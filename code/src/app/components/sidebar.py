"""Sidebar component for the Streamlit app."""
import streamlit as st
import ollama

def render_sidebar():
    with st.sidebar:
        st.subheader("Upload Rules PDF")

        # PDF file uploader
        uploaded_file = st.file_uploader(
            "Upload a PDF file",
            type=["pdf"],  # Allow only PDF files
            help="Upload a PDF file for processing"
        )
        
        # Display file details if a file is uploaded
        if uploaded_file is not None:
            st.write("**Uploaded File Details:**")
            st.write(f"Filename: `{uploaded_file.name}`")
            st.write(f"File size: `{uploaded_file.size} bytes`")
        
        return uploaded_file