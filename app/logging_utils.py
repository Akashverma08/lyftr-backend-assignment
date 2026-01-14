import json, time, uuid
from datetime import datetime

def log_request(request, response, latency, extra=None):
    log = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "level": "INFO",
        "request_id": str(uuid.uuid4()),
        "method": request.method,
        "path": request.url.path,
        "status": response.status_code,
        "latency_ms": int(latency * 1000)
    }
    if extra:
        log.update(extra)
    print(json.dumps(log))
