def is_order_request(question):

    question = question.lower()

    keywords = [
        "pesan",
        "order",
        "beli",
        "tambah",
        "tambahkan",
        "mau",
        "ingin",
        "pesanan",
        "pesen",
        "tolong",
        "tambahkan ke keranjang",
        "tambahkan ke cart",
        "masukkan ke keranjang",
        "masukkan ke cart",
    ]

    return any(
        keyword in question
        for keyword in keywords
    )