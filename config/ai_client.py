from groq import Groq
from dotenv import load_dotenv

import streamlit as st
import os

load_dotenv()


@st.cache_resource
def get_groq_client():

    api_key = os.getenv(
        "GROQ_API_KEY"
    )

    if not api_key:
        return None

    return Groq(
        api_key=api_key
    )