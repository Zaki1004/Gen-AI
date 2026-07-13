from utils.order_extractor import (
    extract_order
)

from services.cart_service import (
    build_cart
)

from services.order_service import (
    checkout
)

question = """
2 caramel latte
1 croissant
"""

orders = extract_order(
    question
)

cart, total = build_cart(
    orders
)

order_number = checkout(
    cart,
    total
)

print(
    "ORDER NUMBER:",
    order_number
)