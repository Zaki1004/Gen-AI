from services.cart_memory import (
    add_to_cart,
    get_cart,
    get_total
)

add_to_cart({
    "name": "Caramel Latte",
    "quantity": 2,
    "price": 35000,
    "subtotal": 70000
})

add_to_cart({
    "name": "Croissant",
    "quantity": 1,
    "price": 18000,
    "subtotal": 18000
})

add_to_cart({
    "name": "Caramel Latte",
    "quantity": 1,
    "price": 35000,
    "subtotal": 35000
})

print(get_cart())

print()

print(
    "TOTAL:",
    get_total()
)