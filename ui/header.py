import streamlit as st

from services.cart_session_service import (
    get_cart
)

from services.order_history_service import (
    get_recent_orders
)

from ui.cart import (
    render_cart
)

from ui.history import (
    render_history
)


def render_header():

    # ==========================
    # Load Data
    # ==========================

    cart, total = get_cart()

    orders = get_recent_orders()

    # ==========================
    # Header Layout
    # ==========================

    left, right = st.columns(
        [7, 3],
        vertical_alignment="top"
    )

    with left:

        st.title(
            "☕ CoffeeBot"
        )

        st.caption(
            "AI Coffee Shop Assistant"
        )

    with right:

        history_col, cart_col = st.columns(
            [1,1],
            gap="small",
        )

        with history_col:

            render_history(
                orders
            )

        with cart_col:

            render_cart(
                cart,
                total
            )

    st.divider()