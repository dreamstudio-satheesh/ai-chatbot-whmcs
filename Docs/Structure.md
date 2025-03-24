
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