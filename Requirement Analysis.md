# AI Chatbot & Ticket Answering System for Web Hosting – Requirement Analysis

## ✅ MVP Scope

### 1️⃣ User Authentication & Management

- User login/logout system in **Laravel** Admin Panel.
- Role-based access (Admin, Support Staff).
- Secure password hashing and session management.

### 2️⃣ AI Chatbot with RAG (Retrieval-Augmented Generation)

- Real-time chatbot interface via API (can be embedded on client sites).
- RAG-based retrieval using **FAISS** and **PostgreSQL**.
- Stores and retrieves knowledge base documents for enhanced answers.

### 3️⃣ Chatbot Training & Knowledge Management

- Upload and manage documents from the **Laravel Admin Panel**.
- Store files in **S3-compatible storage** (e.g., AWS S3, Wasabi, DigitalOcean Spaces).
- Generate embeddings (MiniLM-L6-v2) and store in FAISS/PostgreSQL.
- UI to update, delete, and manage stored documents.

### 4️⃣ WHMCS Ticket Answering System

- Connects to WHMCS via API.
- Fetches open tickets.
- Auto-generates responses using AI.
- Allows manual review and approval.
- Updates ticket via WHMCS API.

### 5️⃣ Admin Panel (Laravel)

- Web dashboard for managing:
  - Knowledge base
  - AI settings (temperature, tokens, etc.)
  - Ticket response history
  - User roles and permissions

### 6️⃣ Deployment & Infrastructure

- Single VM deployment using **Docker Compose**.
- Containers for FastAPI, PostgreSQL, FAISS, and Laravel.
- OpenRouter.ai for LLM API integration.

## 🧪 Not Included in MVP (Future Enhancements)

- Multi-tenant SaaS support.
- Real-time live chat with AI + human fallback.
- Voice-based chatbot support (Speech-to-Text).
- Advanced analytics and chatbot usage insights.
- WhatsApp/Email integration for sending responses.
- Feedback-driven fine-tuning and retraining panel.

## 🔗 GitHub

We welcome contributions!

- Repo: [https://github.com/dreamstudio-satheesh/ai-chatbot-whmcs](https://github.com/dreamstudio-satheesh/ai-chatbot-whmcs)

## ✅ Summary

This requirement analysis reflects the updated architecture using **Laravel** for admin control. The system supports AI automation for web hosting support and integrates with WHMCS in a Dockerized environment.

