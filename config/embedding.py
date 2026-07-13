from sentence_transformers import (
    SentenceTransformer
)

import streamlit as st


MODEL_NAME = (
    "all-MiniLM-L6-v2"
)


@st.cache_resource
def get_embedding_model():

    return SentenceTransformer(
        MODEL_NAME
    )