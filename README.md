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

refer to the [Folder Structure](Structure.md).

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

