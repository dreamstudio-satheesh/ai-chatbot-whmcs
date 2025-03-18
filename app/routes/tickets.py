from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.ticket import Ticket
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

@router.post("/tickets", response_model=TicketResponse)
async def create_new_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(subject=ticket.subject, description=ticket.description)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@router.get("/tickets", response_model=List[TicketResponse])
async def fetch_all_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()
