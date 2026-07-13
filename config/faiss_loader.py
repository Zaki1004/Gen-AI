import streamlit as st

from rag.vector_store import (
    load_faiss_index
)


@st.cache_resource
def get_vector_store():

    return load_faiss_index()