import streamlit as st
import requests
import os

# API URL for FastAPI backend
API_URL = "http://ai-chatbot:8000"

st.title("AI Chatbot RAG Management")

# Text Input for Queries
query = st.text_input("Enter a query:")

if st.button("Search Knowledge Base"):
    if query:
        response = requests.get(f"{API_URL}/search", params={"query": query})
        if response.status_code == 200:
            st.write("### Search Results:")
            st.json(response.json())
        else:
            st.error("Failed to fetch results.")
    else:
        st.warning("Please enter a query.")

# Upload Section
st.write("## Upload Documents")
uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{API_URL}/upload", files=files)
    if response.status_code == 200:
        st.success("File uploaded successfully!")
    else:
        st.error("Upload failed.")
