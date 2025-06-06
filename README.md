# ORIC Compliance System

This project provides a backend and frontend structure to manage post-meeting compliance tasks for ORIC-registered Aboriginal corporations. It includes:

- ✅ Flask-based REST API backend
- ✅ React-based frontend (optional integration)
- ✅ MySQL-compatible via Docker
- ✅ GitHub Actions CI pipeline
- ✅ Ready for EC2 or Proxmox deployment

---

## 🚀 Quick Start (Local)

### Prerequisites

- Python 3.10+
- Docker + Docker Compose
- Git

### Local Run (No Docker)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python seed_admin.py
python app.py
```

---

## 🐳 Docker Deployment (EC2 or Proxmox)

### 1. Clone the Repo
```bash
git clone https://github.com/peacedove777/oric-compliance.git
cd oric-compliance
```

### 2. Start Docker Services
```bash
docker-compose up --build
```

This will start:
- `backend` (Flask API)
- `mysql` (or `sqlite` depending on config)
- (Optional) frontend container

---

## ☁ EC2 Deployment (Free Tier)

1. Launch an EC2 instance (Ubuntu 22.04)
2. SSH in:
```bash
ssh ubuntu@your-ec2-ip
```
3. Install:
```bash
sudo apt update && sudo apt install docker.io docker-compose git -y
```
4. Clone + run:
```bash
git clone https://github.com/peacedove777/oric-compliance.git
cd oric-compliance
docker-compose up --build
```

---

## 🔗 Frontend Integration

If connecting from the Anangu Tjuta SaaS frontend:
- API base path: `https://your-ec2-ip/api/`
- Auth can be passed via headers (token/session)
- CORS is preconfigured

---

## 🔐 HTTPS (Production)

For public HTTPS:
- Use NGINX + Certbot or
- Self-signed certs for testing
- Dockerized NGINX config is available under `deploy/nginx.conf`

---

## 🧪 GitHub Actions (CI)

Located in `.github/workflows/ci.yml`, runs on:
- `push`
- `pull_request` to `main`

---

## 🛠 Developed by Anangu Tjuta | MIT License
