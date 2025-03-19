import streamlit as st

# Hardcoded user credentials (for testing purposes)
VALID_USERS = {
    "admin": "admin123",
    "support": "support456"
}

def login(username, password):
    if username in VALID_USERS and VALID_USERS[username] == password:
        st.session_state["authenticated"] = True
        st.session_state["username"] = username
        st.success(f"Welcome, {username}!")
        st.rerun()
    else:
        st.error("Invalid username or password")

def logout():
    st.session_state["authenticated"] = False
    st.rerun()

def login_screen():
    """ Displays the login screen """
    st.title("🔐 Login - AI Chatbot Dashboard")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        login(username, password)
