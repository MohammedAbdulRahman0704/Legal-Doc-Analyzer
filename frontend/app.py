import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="IntelliDoc: Legal Analyzer",
    layout="wide",
    initial_slidebar_state="expanded"
)

# Custom styles fo enterprise look
st.markdown("""
            <style>
            body{
                background-color: #f3f6fb;
            }
            .stTextArea textarea {
                background-color: black;
                border-radius: 10px;
                font-size: 15px;
                border: 1px solid #d1d5db;
            }
            .stButton > button {
                background-color: #205081;
                color: #ffffff;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
            }
            .stButton > button:hover {
                background-color: #153a5b;
            }
            .stFileUploader {
                margin-top: 10px;
            }
            .reportview-container .main footer {visibility: hidden;}
            </style>
            """, unsafe_allow_html=True)

# Header
st.sidebar.title("IntelliDoc: Legal Analyzer")
st.markdown("Levrage LLaMA2 locally to summarize, extract clauses and identify entities from legal or policy content.")

# Section toggles
st.subheader("Select Extraction Options")
col1, col2, col3 = st.columns(3)
with col1:
    do_summary = st.checkbox("Summarize", value=True)
with col2:
    do_clauses = st.checkbox("Extract Key Clauses", value=True)
with col3:
    do_entities = st.checkbox("Identify Named Entities", value=True)

# Input selection
st.subheader("Document Input")
input_type = st.radio("Choose how you'd like to provide input:", ["Text Input", "Upload .txt File"])
text_input = ""

if input_type == "Text Input":
    text_input = st.text_area("Paste your legal document content below:", height=5000)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        text_input = uploaded_file.read().decode("utf-8")
        st.text_area("Document Content", value=text_input, height=5000)

# Analyze Button
if st.button("Run Analysis"):
    if text_input.strip() and (do_summary or do_clauses or do_entities):
        with st.spinner("Running local LLM via Ollama..."):
            # Call the backend API
            try:
                form_data = {
                    "text": text_input,
                    "summary": do_summary,
                    "clauses": do_clauses,
                    "entities": do_entities
                }
                response = requests.post(
                    "http://localhost:8000/analyze/",
                    data=form_data
                )
                response.raise_for_status()
                results = response.json().get("results", {})
                st.success("Document processed successfully!")
                
                # Progress indicator
                progress = 0
                progress_bar = st.progress(progress)
                
                if do_summary and "Summary" in results:
                    progress += 33
                    st.markdown("### Summary")
                    st.code(results["Summary"], language="markdown")
                    progress_bar.progress(progress)
                
                if do_clauses and "Key Clauses" in results:
                    progress += 33
                    st.markdown("### Key Clauses")
                    st.code(results["Key Clauses"], language="markdown")
                    progress_bar.progress(progress)
                
                if do_entities and "Named Entities" in results:
                    progress += 34
                    st.markdown("### Named Entities")
                    st.code(results["Named Entities"], language="markdown")
                    progress_bar.progress(progress)
            
            except requests.RequestException as e:
                st.error(f"Server error: {str(e)}")
    else:
        st.warning("Please provide a legal document and select at least one extraction option.")

# Footer
st.markdown("---")
st.caption("IntelliDoc Legal Analyzer v2.0 | Powered by FastAPI + Streamlit _ Ollama LLaMA 2")
st.markdown("© 2023 IntelliDoc. All rights reserved.")