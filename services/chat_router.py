from services.llm_service import (
    generate_response
)

from utils.order_detector import (
    is_order_request
)

from utils.order_extractor import (
    extract_order
)

from services.cart_service import (
    build_cart
)

from utils.cart_formatter import (
    format_cart
)

from utils.conversation_intent import (
    detect_intent
)

from utils.remove_extractor import (
    extract_remove_item
)

from services.cart_session_service import (
    merge_cart,
    remove_item,
    get_cart,
    clear_cart
)


def route_message(messages):

    question = (
        messages[-1]["content"]
    )

    print("QUESTION:", question)
    print(
        "IS ORDER:",
        is_order_request(question)
    )

    intent = detect_intent(
    question
    )

    if intent == "clear_cart":

        clear_cart()

        return (
            "🛒 Keranjang berhasil dikosongkan"
        )

    if intent == "view_cart":

        cart, total = get_cart()

        return format_cart(
            cart,
            total
        )

    if intent == "remove_item":

        menu_name = (
            extract_remove_item(
                question
            )
        )

        if menu_name:

            remove_item(
                menu_name
            )

            cart, total = (
                get_cart()
            )

            return format_cart(
                cart,
                total
            )

    if is_order_request(
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

        merged_cart, merged_total = (
            get_cart()
        )

        return format_cart(
            merged_cart,
            merged_total
        )

    return generate_response(
        messages
    )