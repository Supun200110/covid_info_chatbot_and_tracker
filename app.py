import streamlit as st
st.set_page_config(
    page_title="🦠 COVID-19 Tracker",
    page_icon="🏠",
    layout="wide"
)
import pandas as pd
import numpy as np


# Main page content
st.title("🏠 About ")
st.write("This is the main page of our Streamlit application.")

# Sidebar
st.sidebar.success("Select a page above.")

# Main content
st.header("Overview")
st.write("""
This application demonstrates a multi-page Streamlit app with the following pages:
- **Covid Tracker**: When you click on this page, you will be able to track covid status in different countries.
- **Chat Bot**: you will be able to chat with a bot and ask questions about covid.

Use the sidebar navigation to switch between pages.
""")
