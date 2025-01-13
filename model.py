from langchain_groq import ChatGroq
import os
import streamlit as st

# Access API key from Streamlit secrets

def model() :
    api_key = st.secrets["api_key"]
    try :
        llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name="llama-3.3-70b-versatile")
        return llm
    except :
        return False