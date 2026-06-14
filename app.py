import streamlit as st
from services.llm_service import generate_response

st.set_page_config(
    page_title="CoffeBot",
    page_icon="☕",
    layout="wide"
)

st.title("☕ CoffeBot")
st.caption("AI Coffee Shop Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(
    "Tanyakan sesuatu tentang kopi..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    answer = generate_response(
        st.session_state.messages
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)