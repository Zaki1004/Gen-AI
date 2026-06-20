import streamlit as st


def init_cart():

    if "cart" not in st.session_state:

        st.session_state.cart = []

    if "cart_total" not in st.session_state:

        st.session_state.cart_total = 0


def save_cart(
    cart,
    total
):

    st.session_state.cart = cart

    st.session_state.cart_total = total


def get_cart():

    return (
        st.session_state.get(
            "cart",
            []
        ),
        st.session_state.get(
            "cart_total",
            0
        )
    )


def clear_cart():

    st.session_state.cart = []

    st.session_state.cart_total = 0

def merge_cart(
    new_cart,
    new_total
):

    current_cart = (
        st.session_state.get(
            "cart",
            []
        )
    )

    current_total = (
        st.session_state.get(
            "cart_total",
            0
        )
    )

    for new_item in new_cart:

        found = False

        for current_item in current_cart:

            if (
                current_item["name"]
                ==
                new_item["name"]
            ):

                current_item["quantity"] += (
                    new_item["quantity"]
                )

                current_item["subtotal"] += (
                    new_item["subtotal"]
                )

                found = True

                break

        if not found:

            current_cart.append(
                new_item
            )

    st.session_state.cart = (
        current_cart
    )

    st.session_state.cart_total = (
        current_total +
        new_total
    )
    

def remove_item(menu_name):

    current_cart = (
        st.session_state.get(
            "cart",
            []
        )
    )

    new_cart = []

    total = 0

    for item in current_cart:

        if (
            item["name"].lower()
            !=
            menu_name.lower()
        ):

            new_cart.append(item)

            total += (
                item["subtotal"]
            )

    st.session_state.cart = (
        new_cart
    )

    st.session_state.cart_total = (
        total
    )