import streamlit as st

from services.llm_service import (
    generate_response
)

from services.chat_checkout_service import (
    create_demo_checkout
)

from services.payment_service import (
    get_order,
    pay_order
)

st.set_page_config(
    page_title="CoffeeBot",
    page_icon="☕",
    layout="wide"
)

st.title("☕ CoffeeBot")
st.caption("AI Coffee Shop Assistant")

# ==========================
# Checkout Demo
# ==========================

st.divider()

st.subheader(
    "🛒 Demo Checkout"
)

if st.button(
    "Checkout Demo"
):

    result = create_demo_checkout()

    st.session_state.payment_token = (
        result["payment_token"]
    )

    st.success(
        "Order berhasil dibuat"
    )

    st.rerun()

# ==========================
# Payment Panel
# ==========================

if "payment_token" in st.session_state:

    st.divider()

    st.subheader(
        "💳 Pembayaran"
    )

    token = (
        st.session_state.payment_token
    )

    order = get_order(token)

    if order:

        order_id = order[0]
        status = order[1]
        total_price = order[2]

        st.write(
            f"Order ID: {order_id}"
        )

        st.metric(
            "Total Pembayaran",
            f"Rp{total_price:,}"
        )

        if status == "paid":

            st.success(
                "✅ Status: PAID"
            )

        else:

            st.warning(
                "⏳ Status: UNPAID"
            )

            if st.button(
                "💳 Bayar Sekarang"
            ):

                pay_order(token)

                st.success(
                    "Pembayaran berhasil"
                )

                st.rerun()

# ==========================
# Chatbot
# ==========================

if "messages" not in st.session_state:

    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

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

    with st.chat_message(
        "user"
    ):
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

    with st.chat_message(
        "assistant"
    ):
        st.markdown(answer)