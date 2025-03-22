"""
Streamlit application for Data Profiling

"""

import streamlit as st
from components.sidebar import render_sidebar

# Render the sidebar
uploaded_file = render_sidebar()

st.title("Data Profiler")
st.write("Welcome to Gen AI data profiling to make your work easier!")