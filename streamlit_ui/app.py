import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Hardcoded user credentials (for testing purposes)
VALID_USERS = {
    "admin": "admin123",  # username: password
    "support": "support456"
}

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Login function
def login(username, password):
    if username in VALID_USERS and VALID_USERS[username] == password:
        st.session_state["authenticated"] = True
        st.session_state["username"] = username
        st.success(f"Welcome, {username}!")
        st.rerun()
    else:
        st.error("Invalid username or password")

# Logout function
def logout():
    st.session_state["authenticated"] = False
    st.rerun()

# Streamlit UI
st.title("🔐 Login - AI Chatbot Dashboard")

if not st.session_state["authenticated"]:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
    
    if submit:
        login(username, password)
else:
    st.sidebar.button("Logout", on_click=logout)
    st.success(f"Logged in as {st.session_state['username']}")
    st.write("Welcome to the AI Chatbot Dashboard!")
