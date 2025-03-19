import streamlit as st
import requests
import config

def upload_ui():
    """ Upload Document UI """
    st.header("📤 Upload Documents")

    uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])

    if uploaded_file:
        with st.spinner("Uploading file..."):
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(f"{config.API_URL}/upload", files=files)
            if response.status_code == 200:
                st.success(f"✅ `{uploaded_file.name}` uploaded successfully!")
            else:
                st.error("Upload failed. Please try again.")
