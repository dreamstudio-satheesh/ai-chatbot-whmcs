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
class TicketRequest(BaseModel):
    ticket_id: str

# WHMCS API Function
def fetch_whmcs_tickets():
    WHMCS_API_URL = os.getenv("WHMCS_API_URL")
    WHMCS_API_KEY = os.getenv("WHMCS_API_KEY")
    WHMCS_API_IDENTIFIER = os.getenv("WHMCS_API_IDENTIFIER")

    if not WHMCS_API_URL or not WHMCS_API_KEY or not WHMCS_API_IDENTIFIER:
        raise HTTPException(status_code=500, detail="Missing WHMCS API credentials")
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "identifier": WHMCS_API_IDENTIFIER,
        "secret": WHMCS_API_KEY,
        "action": "GetTickets",
        "responsetype": "json"
    }
    
    try:
        response = requests.post(WHMCS_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("tickets", [])
    except requests.exceptions.RequestException as e:
        print(f"WHMCS API Error: {e}")
        raise HTTPException(status_code=500, detail=f"WHMCS API error: {str(e)}")

# Tickets API Endpoint
@router.get("/tickets")
def get_tickets():
    tickets = fetch_whmcs_tickets()
    return {"tickets": tickets}