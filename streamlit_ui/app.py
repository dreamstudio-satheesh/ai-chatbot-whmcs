import streamlit as st
from login import login_screen, logout
from rag_search import search_ui
from rag_upload import upload_ui
from tickets import tickets_ui
from ticket_detail import ticket_detail_ui
import config

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "selected_ticket" not in st.session_state:
    st.session_state["selected_ticket"] = None

# Login Screen
if not st.session_state["authenticated"]:
    login_screen()
    st.stop()

# Sidebar Navigation
st.set_page_config(page_title="AI Chatbot - WHMCS Support", layout="wide")

st.sidebar.header(f"👤 Logged in as: {st.session_state['username']}")
st.sidebar.button("Logout", on_click=logout)

st.sidebar.header("📌 Navigation")
page = st.sidebar.radio("Go to", ["Search Knowledge Base", "Upload Document", "Ticket Management"])

# Ticket Management System
if page == "Ticket Management":
    if st.session_state["selected_ticket"]:
        ticket_detail_ui(st.session_state["selected_ticket"])
        if st.button("🔙 Back to Tickets"):
            st.session_state["selected_ticket"] = None
            st.rerun()
    else:
        tickets_ui()
elif page == "Search Knowledge Base":
    search_ui()
elif page == "Upload Document":
    upload_ui()
