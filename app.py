import streamlit as st
import PyPDF2
import openai

st.title("📘 AI Study Notes Generator")

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    if st.button("Generate Notes"):
        with st.spinner("AI is generating notes..."):
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": f"Summarize this into study notes:\n\n{text}"}],
                temperature=0.5
            )
            notes = response["choices"][0]["message"]["content"]
            st.subheader("📒 Study Notes")
            st.write(notes)
