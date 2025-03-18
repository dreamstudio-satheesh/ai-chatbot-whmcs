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
│
│── app/                           # Core FastAPI backend
│   ├── models/                     # Database models (PostgreSQL)
│   │   ├── ticket.py                # Ticket model for WHMCS integration
│   │
│   ├── routes/                     # API routes for the FastAPI application
│   │   ├── chatbot.py               # Route for chatbot interactions
│   │   ├── tickets.py               # Route for handling support tickets
│   │
│   ├── services/                   # Business logic layer for chatbot & tickets
│   │   ├── chatbot.py               # Chatbot processing and logic
│   │
│   ├── utils/                      # Utility functions and database handling
│   │   ├── database.py              # Database connection and helper functions
│   │   ├── __init__.py              # Package initialization file
│   │
│   ├── Dockerfile                   # Docker setup for FastAPI backend
│   ├── main.py                       # FastAPI entry point
│   ├── requirements.txt              # Python dependencies for FastAPI
│
│── db/                              # Database-related files
│   ├── init.sql                      # SQL initialization script
│   ├── faiss_store/                   # FAISS vector storage for RAG
│
│── streamlit_ui/                    # Streamlit-based UI for managing RAG
│   ├── app.py                        # Streamlit application entry point
│   ├── Dockerfile                    # Docker setup for Streamlit UI
│   ├── requirements.txt               # Python dependencies for Streamlit UI
│
│── .env                              # Environment variables (secrets/configs)
│── .env.example                      # Example environment variables file
│── .gitignore                        # Ignore unnecessary files in Git
│── docker-compose.yml                # Docker Compose file to manage services
│── Installation.md                    # Setup and installation guide
│── License                            # Project license details
│── README.md                          # Project documentation

```

## Installation & Setup
For detailed installation steps, refer to the [Installation Guide](Installation.md).

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

