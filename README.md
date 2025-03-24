# AI Chatbot & Ticket Answering System for Web Hosting

## Overview
This project is an AI-powered chatbot and ticket answering system designed for web hosting companies. The system integrates with WHMCS for automated support responses and runs efficiently on a **single VM using Docker**.

## Features
- **AI Chatbot**: Handles common web hosting queries using OpenRouter.ai LLM.
- **Ticket Answering System**: AI-assisted responses for WHMCS support tickets.
- **Retrieval-Augmented Generation (RAG)**: Uses PostgreSQL & FAISS for knowledge retrieval.
- **WHMCS Integration**: Automates ticket management via WHMCS API.
- **Admin Panel (Laravel)**: A Laravel-based web dashboard for managing the knowledge base and chatbot settings.
- **Dockerized Deployment**: Runs all services (FastAPI, PostgreSQL, FAISS, and Laravel) inside Docker.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Admin Panel**: Laravel (PHP)
- **AI Integration**: OpenRouter.ai API
- **Database**: PostgreSQL (structured data) + FAISS (vector search for knowledge base)
- **Deployment**: Docker (Single VM)
- **WHMCS API**: Used for ticket fetching and updates

## Folder Structure

Please refer to the [Folder Structure](Docs/Structure.md) File.

## Installation & Setup
For detailed installation steps, refer to the [Installation Guide](Docs/Installation.md) File.

## Usage
### API Endpoints (FastAPI)
- **Chatbot Query:** `POST /chat`  
  **Input:** `{ "message": "How do I renew my domain?" }`
- **Ticket Answering (WHMCS Integration):** `GET /tickets`  
  Fetches open WHMCS tickets for AI suggestions.
- **Knowledge Base Management (API):** `POST /add_document`  
  Uploads new knowledge base entries for FAISS retrieval.

### WHMCS Plugin Integration
- Uses WHMCS API to fetch open tickets.
- AI auto-suggests responses for admin review.
- Approved responses update tickets via WHMCS API.

## Contributing
We welcome contributions! To get started:
1. Fork the repository from [GitHub](https://github.com/dreamstudio-satheesh/ai-chatbot-whmcs).
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Submit a pull request with a brief description of your changes.

Your contributions help improve the project for everyone. Thank you!

## Future Enhancements
- Multi-Language Support for chatbot.
- Real-time WebSocket API for live AI assistance.
- AI-powered knowledge base auto-updates.

## License
This project is licensed under the MIT License.

