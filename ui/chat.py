import streamlit as st
import time

from agents.coffee_agent import (
    run_agent
)


def render_chat():

    # ==========================
    # CHAT HISTORY
    # ==========================

    for message in st.session_state.messages:

        avatar = (
            "☕"
            if message["role"] == "assistant"
            else "👤"
        )

        with st.chat_message(
            message["role"],
            avatar=avatar
        ):

            st.markdown(
                message["content"]
            )

    # ==========================
    # CHAT INPUT
    # ==========================

    prompt = st.chat_input(
        "Tanyakan sesuatu tentang kopi..."
    )

    if not prompt:

        return

    # ==========================
    # USER MESSAGE
    # ==========================

    st.session_state.messages.append(

        {

            "role": "user",

            "content": prompt

        }

    )

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(
            prompt
        )

    # ==========================
    # ASSISTANT
    # ==========================



    with st.chat_message(
        "assistant",
        avatar="☕"
    ):

        with st.spinner(
            "CoffeeBot sedang berpikir..."
        ):

            answer = run_agent(
                prompt
            )

        placeholder = st.empty()

        displayed_text = ""

        for word in answer.split():

            displayed_text += word + " "

            placeholder.markdown(
                displayed_text + "▌"
            )

            time.sleep(
                0.03
            )

        placeholder.markdown(
            displayed_text
        )

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": answer

        }

    )

    st.rerun()