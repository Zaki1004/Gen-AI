import streamlit as st

from agents.coffee_agent import (
    run_agent
)

from services.order_service import (
    checkout
)

from services.payment_service import (
    get_order,
    pay_order
)

from services.cart_session_service import (
    init_cart,
    get_cart,
    clear_cart
)

from services.order_history_service import (
    get_recent_orders
)

st.set_page_config(
    page_title="CoffeeBot",
    page_icon="☕",
    layout="wide"
)

st.title("☕ CoffeeBot")
st.caption("AI Coffee Shop Assistant")

init_cart()


# ==========================
# Checkout Demo
# ==========================

st.divider()

st.subheader(
    "🛒 Checkout"
)

cart, total = get_cart()

if cart:

    st.success(
        f"🛒 {len(cart)} item dalam keranjang"
    )

    st.write(
        "Isi Keranjang:"
    )

    for item in cart:

        st.write(
            f"• {item['name']} "
            f"x{item['quantity']}"
        )

    st.metric(
        "Total",
        f"Rp{total:,}"
    )

    if st.button(
        "Checkout Keranjang"
    ):

        result = checkout(
            cart,
            total
        )

        st.session_state.payment_token = (
            result["payment_token"]
        )

        clear_cart()

        st.success(
            "Order berhasil dibuat"
        )

else:

    st.info(
        "Keranjang masih kosong"
    )

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

# ORDER HISTORY

st.divider()

st.subheader(
    "📜 Riwayat Order"
)

orders = get_recent_orders()

for order in orders:

    st.write(
        f"Order #{order[0]}"
        f" | Rp{order[1]:,}"
        f" | {order[2]}"
    )              


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

    answer = run_agent(
        prompt
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

    st.rerun()