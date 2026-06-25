from utils.order_extractor import (
    extract_order
)

from services.cart_service import (
    build_cart
)

from services.cart_session_service import (
    merge_cart,
    get_cart
)

from utils.cart_formatter import (
    format_cart
)


def order_tool_node(
    question
):

    orders = extract_order(
        question
    )

    cart, total = build_cart(
        orders
    )

    merge_cart(
        cart,
        total
    )

    cart, total = (
        get_cart()
    )

    return format_cart(
        cart,
        total
    )