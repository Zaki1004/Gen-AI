from utils.order_extractor import (
    extract_order
)

question = (
    "Saya pesan 2 caramel latte 1 espresso"
)

result = extract_order(
    question
)

print(result)