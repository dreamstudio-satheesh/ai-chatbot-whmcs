import requests
import faiss
import numpy as np
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from utils.database import get_db
from sqlalchemy.orm import Session

# Load environment variables
load_dotenv()

router = APIRouter()

# OpenRouter.ai API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is missing in .env file")

# PostgreSQL Connection via SQLAlchemy
from models.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chatbot_response(request: ChatRequest):
    return {"response": f"Hello! You said: {request.message}"}
