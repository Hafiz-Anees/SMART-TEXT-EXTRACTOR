import streamlit as st

def sidebar():
    st.sidebar.title("📄 Smart Text Extractor Tool")
    st.sidebar.write("Upload your file and extract text easily.")

def main_header():
    st.title("✨ Smart Text Extractor")
    st.markdown("Upload your file and extract text instantly.")

def file_uploader():
    return st.file_uploader("📂 Upload file", type=['pdf'])

def show_results(text, pages):
    st.success("Extraction Complete ✅")

    col1, col2 = st.columns(2)
    col1.metric("Pages", pages)
    col2.metric("Characters", len(text))

    st.subheader("📜 Extracted Text")
    st.text_area("Result", text, height=400)

def download_button(text):
    st.download_button(
        label="⬇️ Download Text",
        data=text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )

