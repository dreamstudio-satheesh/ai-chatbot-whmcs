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

@router.get("/tickets", response_model=List[TicketResponse])
async def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return tickets
