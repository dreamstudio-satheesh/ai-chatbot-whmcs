from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from models.ticket import Ticket
from typing import List
from pydantic import BaseModel

router = APIRouter()

class TicketCreate(BaseModel):
    subject: str
    description: str

class TicketResponse(TicketCreate):
    id: int
    status: str
    created_at: str

    class Config:
        from_attributes = True


@router.get("/tickets")
async def get_tickets():
    return {"tickets": ["Hello! This is a sample ticket response."]}