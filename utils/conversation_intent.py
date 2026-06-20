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

    return "normal"