import streamlit as st
import requests
import PyPDF2
import base64
import tempfile

# Set page configuration
st.set_page_config(page_title="IntelliDoc Legal Analyzer API", layout="centered")

# Sidebar instructions
st.sidebar.title("How It Works")
st.sidebar.write("""
1. Upload a PDF or enter legal text manually.
2. Click **Analyze** to process the document.
3. View:
   - Summary
   - Key Clauses
   - Named Entities
""")
st.sidebar.write("*Ensure FastAPI server is running on http://localhost:8000*")

# Title and input
st.title("IntelliDoc Legal Analyzer API")
st.markdown("*Analyze legal documents using LLaMA2 via FastAPI.*")

# File uploader
uploaded_file = st.file_uploader("Upload a legal PDF file:", type="pdf")
extracted_text = ""

# Display PDF if uploaded
if uploaded_file is not None:
    st.subheader("Uploaded PDF Preview")

    # Show iframe preview using base64 encoding
    base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Extract text from PDF
    uploaded_file.seek(0)  # Reset file pointer
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        extracted_text += page.extract_text() or ""

# Manual text input (optional)
text_input = st.text_area("Or paste legal text here:", height=200, placeholder="Enter legal content...")

# Decide which input to use
final_text = extracted_text.strip() if extracted_text else text_input.strip()

# Analyze button
if st.button("Analyze"):
    if final_text:
        with st.spinner("Analyzing document..."):
            try:
                response = requests.post("http://localhost:8000/analyze/", data={"text": final_text})
                response.raise_for_status()
                results = response.json()

                st.subheader("Summary")
                with st.expander("View Summary"):
                    st.write(results.get("summary", "No summary found."))

                st.subheader("Key Clauses")
                with st.expander("View Key Clauses"):
                    st.write(results.get("clauses", "No key clauses detected."))

                st.subheader("Named Entities")
                with st.expander("View Named Entities"):
                    st.write(results.get("entities", "No named entities found."))

            except requests.exceptions.RequestException as e:
                st.error(f"Error contacting backend: {e}")
    else:
        st.warning("⚠ Please upload a PDF or enter text before analyzing.")

# Footer
st.markdown("---")
st.markdown("Built for legal insights using LLMs")