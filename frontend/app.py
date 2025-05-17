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

