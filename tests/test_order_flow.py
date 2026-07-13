from services.order_flow import (
    process_order
)

print(
    process_order(
        "Saya mau 2 caramel latte"
    )
)

print()

print(
    process_order(
        "Tambah 1 croissant"
    )
)

print()

print(
    process_order(
        "checkout"
    )
)