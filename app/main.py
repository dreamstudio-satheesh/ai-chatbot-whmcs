from fastapi import FastAPI
from routes import tickets, chatbot

app = FastAPI(title="AI Chatbot & Ticket Answering System")

# Include API Routes
app.include_router(tickets.router, prefix="/api")
app.include_router(chatbot.router, prefix="/api")



@app.get("/")
async def root():
    return {"message": "AI Chatbot API is running!"}
