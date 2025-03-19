import streamlit as st
import requests
import config

def ticket_detail_ui(ticket_id):
    """ Display a single ticket with reply functionality """
    st.header(f"📝 Ticket #{ticket_id}")

    # Fetch ticket details
    response = requests.get(f"{config.API_URL}/ticket/{ticket_id}")

    if response.status_code == 200:
        ticket = response.json()

        st.write(f"**Subject:** {ticket['subject']}")
        st.write(f"**Status:** {ticket['status']}")
        st.write("---")
        
        # Show previous replies
        st.write("### 📨 Ticket Replies")
        for reply in ticket.get("replies", []):
            st.markdown(f"**{reply['author']} ({reply['timestamp']}):**")
            st.info(reply["message"])
        
        # Reply section
        st.write("---")
        st.write("### ✍️ Add a Reply")
        reply_text = st.text_area("Enter your reply...")

        if st.button("Send Reply"):
            if reply_text:
                response = requests.post(
                    f"{config.API_URL}/ticket/{ticket_id}/reply",
                    json={"message": reply_text}
                )
                if response.status_code == 200:
                    st.success("Reply sent successfully!")
                    st.rerun()
                else:
                    st.error("Failed to send reply.")
            else:
                st.warning("Reply cannot be empty.")

    else:
        st.error("Failed to load ticket details.")
