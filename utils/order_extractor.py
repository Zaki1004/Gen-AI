import re


def extract_order(question):

    question = question.lower()

    orders = []

    pattern = r'(\d+)\s+([a-zA-Z ]+)'

    matches = re.findall(
        pattern,
        question
    )

    for qty, menu_name in matches:

        orders.append({
            "menu_name": menu_name.strip(),
            "quantity": int(qty)
        })

    return orders