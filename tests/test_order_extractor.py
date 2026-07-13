from utils.order_extractor import (
    extract_order
)

question = (
    "Saya mau dua belas caramel latte dan empat espresso"
)

print(
    extract_order(question)
)