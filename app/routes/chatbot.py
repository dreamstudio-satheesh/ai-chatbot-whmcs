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

router = APIRouter()

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


@router.post("/")
async def chatbot_response():
    return {"response": "Hello from AI Chatbot!"}