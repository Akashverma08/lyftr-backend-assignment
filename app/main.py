from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, Field
import hmac, hashlib, time, re
from app.config import WEBHOOK_SECRET
from app.models import init_db, get_db
from app.storage import insert_message
from app.metrics import inc_http, inc_webhook, render_metrics
from app.logging_utils import log_request

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

class WebhookPayload(BaseModel):
    message_id: str = Field(..., min_length=1)
    from_: str = Field(..., alias="from")
    to: str
    ts: str
    text: str | None = Field(None, max_length=4096)

    @staticmethod
    def validate_phone(v):
        if not re.match(r"^\+\d+$", v):
            raise ValueError("Invalid phone")
        return v

@app.middleware("http")
async def metrics_logger(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    latency = time.time() - start
    inc_http(request.url.path, response.status_code)
    log_request(request, response, latency)
    return response

@app.post("/webhook")
async def webhook(request: Request):
    if not WEBHOOK_SECRET:
        raise HTTPException(503)

    body = await request.body()
    signature = request.headers.get("X-Signature")

    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if signature != expected:
        inc_webhook("invalid_signature")
        raise HTTPException(401, detail="invalid signature")

    data = await request.json()
    result = insert_message(data)
    inc_webhook(result)

    return {"status": "ok"}

@app.get("/messages")
def list_messages(limit: int = 50, offset: int = 0):
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM messages ORDER BY ts ASC, message_id ASC LIMIT ? OFFSET ?",
        (limit, offset)
    ).fetchall()
    total = conn.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    conn.close()

    return {
        "data": [dict(r) for r in rows],
        "total": total,
        "limit": limit,
        "offset": offset
    }

@app.get("/stats")
def stats():
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    senders = conn.execute(
        "SELECT from_msisdn as from_, COUNT(*) as count FROM messages GROUP BY from_msisdn ORDER BY count DESC LIMIT 10"
    ).fetchall()
    first, last = conn.execute("SELECT MIN(ts), MAX(ts) FROM messages").fetchone()
    conn.close()

    return {
        "total_messages": total,
        "senders_count": len(senders),
        "messages_per_sender": senders,
        "first_message_ts": first,
        "last_message_ts": last
    }

@app.get("/health/live")
def live():
    return {"status": "ok"}

@app.get("/health/ready")
def ready():
    if not WEBHOOK_SECRET:
        raise HTTPException(503)
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return render_metrics()
