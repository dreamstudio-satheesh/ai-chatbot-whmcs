import requests
import faiss
import numpy as np
import psycopg2
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

router = APIRouter(prefix="/api")

# OpenRouter.ai API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Construct DATABASE_URL from environment variables
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_DB = os.getenv("POSTGRES_DB", "chatbot_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "ai-chatbot-db")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"

# Establish database connection
conn = psycopg2.connect(DATABASE_URL)

cursor = conn.cursor()

# Load FAISS Index
index = faiss.read_index("/app/db/faiss_store/index.faiss")

class ChatRequest(BaseModel):
    message: str

def retrieve_context(query_text):
    """Retrieve relevant documents from FAISS based on user query"""
    # Convert query to vector (placeholder: replace with actual embedding model)
    query_vector = np.random.rand(1536).astype("float32")

    # Search FAISS index
    D, I = index.search(np.array([query_vector]), k=2)
    if I[0][0] == -1:  # No relevant results found
        return None

    # Retrieve text from PostgreSQL based on index
    cursor.execute("SELECT content FROM knowledge_base WHERE id = %s", (I[0][0],))
    context_data = cursor.fetchone()
    
    return context_data[0] if context_data else None

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """Retrieve relevant context & send query to OpenRouter.ai"""
    context = retrieve_context(request.message)
    if context:
        full_query = f"Context: {context}\nUser Query: {request.message}"
    else:
        full_query = request.message

    # Call OpenRouter.ai for response
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        json={"model": "google/gemma-3-27b-it", "messages": [{"role": "user", "content": full_query}]}
    )

    if response.status_code == 200:
        return {"response": response.json()["choices"][0]["message"]["content"]}
    else:
        return {"error": "Failed to generate AI response"}
