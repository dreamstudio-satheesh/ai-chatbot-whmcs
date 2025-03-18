# AI Chatbot & Ticket Answering System for Web Hosting

## Overview
This project is an AI-powered chatbot and ticket answering system designed for web hosting companies. The system integrates with WHMCS for automated support responses and runs efficiently on a **single VM using Docker**.

## Features
- **AI Chatbot**: Handles common web hosting queries using OpenRouter.ai LLM.
- **Ticket Answering System**: AI-assisted responses for WHMCS support tickets.
- **Retrieval-Augmented Generation (RAG)**: Uses PostgreSQL & FAISS for knowledge retrieval.
- **WHMCS Integration**: Automates ticket management via WHMCS API.
- **Admin UI (Optional)**: Streamlit-based interface for managing the knowledge base.
- **Dockerized Deployment**: Runs all services (FastAPI, PostgreSQL, FAISS, and Streamlit) inside Docker.

## Tech Stack
- **Backend**: FastAPI (Python)
- **AI Integration**: OpenRouter.ai API
- **Database**: PostgreSQL (structured data) + FAISS (vector search for knowledge base)
- **Deployment**: Docker (Single VM)
- **Admin Panel**: Streamlit (for knowledge base management)
- **WHMCS API**: Used for ticket fetching and updates

## Folder Structure
```
ai-chatbot-whmcs/
│── app/                 # Main application folder
│   ├── models/          # Database models (PostgreSQL)
│   ├── routes/          # API endpoints (FastAPI)
│   ├── services/        # Business logic (Chatbot, WHMCS API, FAISS)
│   ├── utils/           # Helper functions
│   ├── __init__.py
│   ├── main.py          # FastAPI entry point
│── db/                  # Database-related files
│── faiss_store/         # FAISS index storage
│── streamlit_ui/        # Streamlit-based admin panel (Optional)
│── .env                 # Environment variables
│── Dockerfile           # FastAPI Docker configuration
│── docker-compose.yml   # Docker Compose setup
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

## Installation & Setup
### 1. Clone the Repository
```bash
git clone <repo-url>
cd ai-chatbot-whmcs
```

### 2. Set Up Environment Variables
Create a `.env` file with database credentials:
```env
DATABASE_URL=postgresql://postgres:password@postgres:5432/ai_db
WHMCS_API_URL=<your-whmcs-url>
WHMCS_API_KEY=<your-api-key>
```

### 3. Build & Start the Containers
```bash
docker-compose up -d --build
```

### 4. Verify Running Services
```bash
docker ps
```
Expected containers:
- `ai_chatbot_backend` (FastAPI service)
- `postgres_db` (PostgreSQL database)
- `streamlit_admin` (Streamlit UI, if enabled)

## Usage
### API Endpoints (FastAPI)
- **Chatbot Query:** `POST /chat`  
  **Input:** `{ "message": "How do I renew my domain?" }`
- **Ticket Answering (WHMCS Integration):** `GET /tickets`  
  Fetches open WHMCS tickets for AI suggestions.
- **Admin Knowledge Base Management:** `POST /add_document`  
  Uploads new knowledge base entries for FAISS retrieval.

### WHMCS Plugin Integration
- Uses WHMCS API to fetch open tickets.
- AI auto-suggests responses for admin review.
- Approved responses update tickets via WHMCS API.

## Future Enhancements
- Multi-Language Support for chatbot.
- Real-time WebSocket API for live AI assistance.
- AI-powered knowledge base auto-updates.

## License
This project is licensed under the MIT License.

