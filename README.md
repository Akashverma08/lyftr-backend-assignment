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

.
├── app/
│ ├── main.py
│ ├── config.py
│ ├── logging_utils.py
│ ├── metrics.py
│ ├── models.py
│ └── storage.py
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

```bash
docker --version
docker compose version
