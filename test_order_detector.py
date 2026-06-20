from utils.order_detector import (
    is_order_request
)

print(
    is_order_request(
        "Saya pesan 2 caramel latte"
    )
)

print(
    is_order_request(
        "Apa itu espresso?"
    )
)