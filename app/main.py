from fastapi import FastAPI
from routes import tickets, chatbot

router = FastAPI(title="AI Chatbot & Ticket Answering System")

# Include API Routes
router.include_router(tickets.router, prefix="/api")
router.include_router(chatbot.router) 



@router.get("/")
async def root():
    return {"message": "AI Chatbot API is running!"}
