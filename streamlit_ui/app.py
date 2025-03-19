import streamlit as st
from login import login_screen, logout
from rag_search import search_ui
from rag_upload import upload_ui
import config

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ----------------- LOGIN SCREEN -----------------
if not st.session_state["authenticated"]:
    login_screen()  # Call login UI
    st.stop()  # Stop further UI rendering if not authenticated

# ----------------- MAIN UI AFTER LOGIN -----------------
st.set_page_config(page_title="RAG Management", layout="wide")

st.sidebar.header(f"👤 Logged in as: {st.session_state['username']}")
st.sidebar.button("Logout", on_click=logout)

st.title("🔍 AI Chatbot - RAG Management")

# Sidebar Navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Search Knowledge Base", "Upload Document"])

# Load the selected module
if page == "Search Knowledge Base":
    search_ui()
elif page == "Upload Document":
    upload_ui()
