import streamlit as st
# from styles import apply_styles
from ui import sidebar, main_header, file_uploader, show_results, download_button
from logic import extract_text_from_pdf


# Page config
st.set_page_config(page_title="Text Extractor", layout="wide")

# UI sections
sidebar()
main_header()

uploaded_file = file_uploader()

# Main logic
if uploaded_file is not None:
    
    text, pages = extract_text_from_pdf(uploaded_file)

    show_results(text, pages)
    download_button(text)

