import streamlit as st

from services.cart_session_service import (
    init_cart
)

from ui.header import (
    render_header
)

from ui.chat import (
    render_chat
)

from ui.welcome import (
    init_welcome
)

from ui.theme import (
    apply_theme
)

st.set_page_config(

    page_title="CoffeeBot",

    page_icon="☕",

    layout="wide"

)

apply_theme()

init_cart()

init_welcome()

render_header()

render_chat()