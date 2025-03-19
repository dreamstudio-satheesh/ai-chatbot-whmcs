import streamlit as st
import requests
import config
from ticket_detail import ticket_detail_ui

def tickets_ui():
    """ Display all tickets """
    st.header("📋 Support Tickets")

    # Fetch tickets from the API
    response = requests.get(f"{config.API_URL}/tickets")

    if response.status_code == 200:
        tickets = response.json()
        
        if not tickets:
            st.warning("No tickets found.")
            return
        
        # Display tickets in a table
        st.write("### Open Tickets")
        for ticket in tickets:
            ticket_id = ticket["id"]
            subject = ticket["subject"]
            status = ticket["status"]
            
            # Clickable button for each ticket
            if st.button(f"🔹 {ticket_id}: {subject} ({status})"):
                st.session_state["selected_ticket"] = ticket_id
                st.rerun()
    
    else:
        st.error("Failed to fetch tickets.")

