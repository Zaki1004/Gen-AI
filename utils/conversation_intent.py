def detect_intent(question):

    question = question.lower()

    if any(
        word in question
        for word in [
            "checkout",
            "bayar",
            "selesai"
        ]
    ):
        return "checkout"

    if any(
        word in question
        for word in [
            "kosongkan keranjang",
            "clear cart",
            "hapus semua"
        ]
    ):
        return "clear_cart"

    if any(
        word in question
        for word in [
            "hapus",
            "remove",
            "batalkan"
        ]
    ):
        return "remove_item"

    if any(
        word in question
        for word in [
            "tambah",
            "tambahkan"
        ]
    ):
        return "add_item"

    if any(
        word in question
        for word in [
            "keranjang",
            "cart",
            "lihat pesanan",
            "lihat keranjang",
            "isi keranjang",
            "lihat pesanan saya",
            "lihat order",
            "lihat order saya",
        ]
    ):
        return "view_cart"

    return "normal"