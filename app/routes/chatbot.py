from fastapi import APIRouter
from app.services.chatbot import chat_with_ai

router = APIRouter()

@router.get("/chat")
async def chatbot_response(query: str):
    response = chat_with_ai(query)
    return {"response": response}
