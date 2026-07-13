from services.order_service import (
    checkout
)

cart = [
    {
        "name": "Caramel Latte",
        "quantity": 2,
        "subtotal": 70000
    }
]

result = checkout(
    cart,
    70000
)

print(result)