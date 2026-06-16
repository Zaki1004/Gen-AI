from utils.order_extractor import (
    extract_order
)

from services.cart_service import (
    build_cart
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

print(cart)

print()

print(
    "TOTAL:",
    total
)