from utils.order_extractor import (
    extract_order
)

from services.cart_service import (
    build_cart
)

question = (
    "Saya pesan 2 caramel latte 1 espresso"
)

orders = extract_order(
    question
)

print("ORDERS:")
print(orders)

cart, total_price = build_cart(
    orders
)

print("\nCART:")
print(cart)

print("\nTOTAL:")
print(total_price)