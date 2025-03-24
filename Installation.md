# Installation Guide

## Prerequisites

Before setting up the project, ensure your system meets the following requirements:

- Debian 12 (or compatible Linux distribution)
- Docker & Docker Compose installed
- Git installed

## Step 1: Update System

```bash
sudo apt update && sudo apt upgrade -y
```

## Step 2: Install Required Packages

```bash
sudo apt install -y curl wget git
```

## Step 3: Install Docker

### 3.1 Add Docker’s Official GPG Key

```bash
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo tee /etc/apt/keyrings/docker.asc > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### 3.2 Set Up Docker Repository

```bash
echo "echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
```

### 3.3 Install Docker & Docker Compose

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 3.4 Verify Docker Installation

```bash
docker --version
docker compose version
```

## Step 4: Clone the Repository

```bash
cd /home/
git clone https://github.com/dreamstudio-satheesh/ai-chatbot-whmcs.git
cd ai-chatbot-whmcs
```

## Step 5: Configure Environment Variables

Create a `.env` file and add your configurations:

```bash
echo "DATABASE_URL=postgresql://postgres:password@postgres:5432/ai_db" > .env
echo "WHMCS_API_URL=<your-whmcs-url>" >> .env
echo "WHMCS_API_KEY=<your-api-key>" >> .env
```

## Step 6: Build & Start the Containers

```bash
docker-compose up -d --build
```

## Step 7: Verify Running Containers

```bash
docker ps
```

Expected containers:

- `ai_chatbot_backend` (FastAPI service)
- `postgres_db` (PostgreSQL database)

## Step 8: Access the Services

- **FastAPI Backend:** `http://<server-ip>:8000`
- **Streamlit UI (if enabled):** `http://<server-ip>:8501`
- **PostgreSQL Database:** Connect via `postgresql://postgres:password@<server-ip>:5432/ai_db`

## Troubleshooting

- Run `docker logs ai_chatbot_backend` to check backend logs.
- Restart services using `docker-compose restart` if needed.
- Ensure firewall allows necessary ports (`8000`, `8501`, `5432`).

