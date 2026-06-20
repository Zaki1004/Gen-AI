NUMBER_MAP = {
    "satu": 1,
    "dua": 2,
    "tiga": 3,
    "empat": 4,
    "lima": 5,
    "enam": 6,
    "tujuh": 7,
    "delapan": 8,
    "sembilan": 9,
    "sepuluh": 10,
    "sebelas": 11,
    "dua belas": 12,
    "tiga belas": 13,
    "empat belas": 14,
    "lima belas": 15,
    "enam belas": 16,
    "tujuh belas": 17,
    "delapan belas": 18,
    "sembilan belas": 19,
    "dua puluh": 20
}


def replace_text_numbers(text):

    text = text.lower()

    # sorting penting supaya
    # "dua belas" diproses dulu
    # sebelum "dua"

    sorted_numbers = sorted(
        NUMBER_MAP.items(),
        key=lambda x: len(x[0]),
        reverse=True
    )

    for word, number in sorted_numbers:

        text = text.replace(
            word,
            str(number)
        )

    return text