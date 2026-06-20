def is_order_request(question):

    question = question.lower()

    keywords = [
        "pesan",
        "order",
        "beli",
        "tambah",
        "tambahkan"
    ]

    return any(
        keyword in question
        for keyword in keywords
    )