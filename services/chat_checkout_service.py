from services.order_service import (
    checkout
)

def create_demo_checkout():

    cart = [
        {
            "name": "Caramel Latte",
            "quantity": 2,
            "subtotal": 70000
        }
    ]

    return checkout(
        cart,
        70000
    )