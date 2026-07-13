def is_order_request(question):

    question = question.lower()

    keywords = [

        # Add Item
        "pesan",
        "order",
        "beli",
        "tambah",
        "tambahkan",
        "mau",
        "ingin",
        "pesanan",
        "pesen",

        # Cart
        "keranjang",
        "cart",

        # Remove
        "hapus",
        "remove",
        "batalkan",
        "kurangi",

        # Checkout
        "checkout",
        "bayar",
        "payment",

        # Clear
        "kosongkan",

    ]

    return any(
        keyword in question
        for keyword in keywords
    )