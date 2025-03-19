import streamlit as st
import requests
import config

def search_ui():
    """ Search UI for Knowledge Base """
    st.header("📖 Search Knowledge Base")

    query = st.text_input("Enter a query:")

    if st.button("🔎 Search"):
        if query:
            response = requests.get(f"{config.API_URL}/search", params={"query": query})
            if response.status_code == 200:
                results = response.json()
                if results:
                    st.success("Results found!")
                    for i, doc in enumerate(results):
                        with st.expander(f"📄 Document {i+1}"):
                            st.write(f"**Title:** {doc.get('title', 'Unknown')}")
                            st.write(f"**Content:** {doc.get('content', 'No content available')}")
                    st.session_state.query_history.append(query)
                else:
                    st.warning("No results found.")
            else:
                st.error("Failed to fetch results. Try again later.")
        else:
            st.warning("Please enter a query.")

    # Display Query History
    if "query_history" in st.session_state and st.session_state.query_history:
        st.subheader("Recent Queries")
        st.write(st.session_state.query_history)
