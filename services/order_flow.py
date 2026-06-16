from utils.order_extractor import (
    extract_order
)

from services.cart_service import (
    build_cart
)

from services.cart_memory import (
    add_to_cart,
    get_cart,
    get_total,
    clear_cart
)

from services.order_service import (
    checkout
)

from utils.cart_formatter import (
    format_cart
)


def process_order(question):

    question = question.lower()

    # =====================
    # CHECKOUT
    # =====================

    if "checkout" in question:

        cart = get_cart()

        if not cart:

            return "Keranjang masih kosong."

        total = get_total()

        order_number = checkout(
            cart,
            total
        )

        clear_cart()

        return (
            "✅ Pesanan berhasil dibuat\n\n"
            f"{order_number}"
        )

    # =====================
    # TAMBAH PESANAN
    # =====================

    orders = extract_order(
        question
    )

    cart, total = build_cart(
        orders
    )

    for item in cart:

        add_to_cart(item)

    return format_cart(
        get_cart(),
        get_total()
    )