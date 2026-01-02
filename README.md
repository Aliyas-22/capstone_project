Internal DevOps Utilities API
 (Capstone Project)

📌 Project Overview

This project is a Python DevOps Capstone Project created as part of my Python for DevOps learning journey.
The goal of this project is to build internal DevOps utility APIs that help monitor basic system health metrics such as CPU usage, disk usage, and overall system status.

The project is developed using FastAPI and follows a clean, modular folder structure, making it easy to understand and extend in the future.

🛠️ Tech Stack Used

Python

FastAPI – for building APIs

Uvicorn – ASGI server

psutil – for system metrics (CPU, Disk, Health)

Virtual Environment (venv)

📁 Project Structure

DevOps-Utilities-API/
│
├── app/
│   ├── api.py
│
├── services/
│   └── metrics_service.py
│
├── routers/
│   └── metrics.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Features Implemented

✅ Basic FastAPI application setup

✅ Health check API for testing

✅ System metrics utility:

CPU usage

Disk usage

System health based on threshold

✅ Clean separation of:

API layer

Service layer

Router layer
