from utils.conversation_intent import (
    detect_intent
)

from utils.order_extractor import (
    extract_order
)

from utils.remove_extractor import (
    extract_remove_item
)

from services.cart_service import (
    build_cart
)

from services.cart_session_service import (
    merge_cart,
    get_cart,
    clear_cart,
    remove_item,
    update_cart_quantity
)

from services.order_service import (
    checkout
)

from utils.cart_formatter import (
    format_cart
)

def order_tool_node(question):

    intent = detect_intent(question)

    # ==========================
    # VIEW CART
    # ==========================

    if intent == "view_cart":

        cart, total = get_cart()

        return format_cart(
            cart,
            total
        )

    # ==========================
    # CLEAR CART
    # ==========================

    if intent == "clear_cart":

        clear_cart()

        return (
            "🗑️ Semua pesanan berhasil dihapus dari keranjang."
        )

    # ==========================
    # REMOVE ITEM
    # ==========================

    if intent == "remove_item":

        menu_name = extract_remove_item(
            question
        )

        if not menu_name:

            return (
                "Menu yang ingin dihapus tidak ditemukan."
            )

        remove_item(
            menu_name
        )

        cart, total = get_cart()

        return format_cart(
            cart,
            total
        )

    # ==========================
    # CHECKOUT
    # ==========================

    if intent == "checkout":

        cart, total = get_cart()

        if not cart:

            return (
                "🛒 Keranjang masih kosong."
            )

        result = checkout(
            cart,
            total
        )

        return (
            f"✅ Checkout berhasil!\n\n"
            f"Order Number : {result['order_number']}"
        )

    # ==========================
    # ADD ITEM
    # ==========================

    orders = extract_order(
        question
    )

    if not orders:

        return (
            "Saya tidak menemukan menu yang ingin dipesan."
        )

    cart, total = build_cart(
        orders
    )

    merge_cart(
        cart,
        total
    )

    cart, total = get_cart()

    return format_cart(
        cart,
        total
    )

    # UPDATE QUANTITY

    if intent == "update_quantity":

    result = extract_remove_item(
        question
    )

    if not result:

        return (
            "Menu tidak ditemukan."
        )

    update_cart_quantity(

        result["menu"],

        result["quantity"]

    )

    cart, total = get_cart()

    return format_cart(
        cart,
        total
    )