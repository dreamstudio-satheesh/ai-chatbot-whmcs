import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Define API Router
router = APIRouter()

# Define Request Model
class ChatRequest(BaseModel):
    question: str

# OpenRouter API Function
def get_ai_response(prompt: str, model: str = None):
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
    DEFAULT_MODEL = os.getenv("OPENROUTER_MODEL", "google/gemma-3-27b-it")  # Read from .env

    if not OPENROUTER_API_KEY:
        raise HTTPException(status_code=500, detail="Missing OpenRouter API key")
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model if model else DEFAULT_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }
    
    try:
        response = requests.post(OPENROUTER_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
    except requests.exceptions.RequestException as e:
        print(f"OpenRouter API Error: {e}")  # Logging the error
        raise HTTPException(status_code=500, detail=f"OpenRouter AI error: {str(e)}")

# Chatbot API Endpoint
@router.post("/chat")
def chat(request: ChatRequest):
    response = get_ai_response(request.question)
    return {"response": response}
