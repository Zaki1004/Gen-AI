from utils.order_extractor import (
    extract_order
)

question = (
    "Saya pesan 2 caramel latte, 1 croissant, dan 1 cappuccino."
)

print(
    extract_order(question)
)