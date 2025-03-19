import requests
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from urllib.parse import urlencode

# Load environment variables
load_dotenv()

# Define API Router
router = APIRouter()

# Define Request Model
class TicketRequest(BaseModel):
    ticket_id: int

# WHMCS API Function
def get_whmcs_tickets():
    WHMCS_API_URL = os.getenv("WHMCS_API_URL")
    WHMCS_API_KEY = os.getenv("WHMCS_API_KEY")  # Admin username
    WHMCS_API_IDENTIFIER = os.getenv("WHMCS_API_IDENTIFIER")  # Admin password (or hashed)
    
    if not WHMCS_API_URL or not WHMCS_API_KEY or not WHMCS_API_IDENTIFIER:
        raise HTTPException(status_code=500, detail="Missing WHMCS API credentials")
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    payload = {
        "action": "GetTickets",
        "identifier": WHMCS_API_KEY,
        "secret": WHMCS_API_IDENTIFIER,
        "responsetype": "json"
    }
    
    try:
        response = requests.post(WHMCS_API_URL, data=urlencode(payload), headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("tickets", [])
    except requests.exceptions.RequestException as e:
        print(f"WHMCS API Error: {e}")  # Logging the error
        raise HTTPException(status_code=500, detail=f"WHMCS API error: {str(e)}")

# WHMCS Ticket API Endpoint
@router.get("/tickets")
def get_tickets():
    tickets = get_whmcs_tickets()
    return {"tickets": tickets}