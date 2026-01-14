# Lyftr Backend Assignment

This repository contains the backend implementation for the **Lyftr AI – Backend Assignment**.
The application is built using **FastAPI** and fully containerized using **Docker**, allowing
any reviewer to easily run it locally with minimal setup.

---

## Project Overview

The backend exposes REST APIs along with health and metrics endpoints.
Docker and Docker Compose are used to ensure the application runs consistently
across different environments.

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Docker & Docker Compose

---

## Project Structure

```text
.
├── app/
│   ├── main.py
│   ├── config.py
│   ├── logging_utils.py
│   ├── metrics.py
│   ├── models.py
│   └── storage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Makefile
├── .gitignore
└── README.md




---

## Prerequisites

Ensure the following are installed on your system:

- Docker Desktop
- WSL2 (for Windows users)

Verify installation:


Clone the repository:
```bash
git clone https://github.com/Shashwatmani/lyftr-backend-assignment.git
cd lyftr

```bash
docker --version
docker compose version


http://localhost:8000

http://localhost:8000/docs



---

### 2 Add **API Endpoints Overview** (Very Important)

Recruiters **love this**. Add:

```md
## Available API Endpoints

| Method | Endpoint          | Description                     |
|------|-------------------|---------------------------------|
| POST | /webhook          | Receive webhook messages        |
| GET  | /messages         | List received messages          |
| GET  | /stats            | Message statistics              |
| GET  | /health/live      | Liveness check                  |
| GET  | /health/ready     | Readiness check                 |
| GET  | /metrics          | Application metrics             |



## Setup Used

- VS Code as the primary code editor
- Docker Desktop with WSL2 backend (Windows)
- Git & GitHub for version control
- GitHub Copilot
- Occasional ChatGPT prompts for guidance and validation
