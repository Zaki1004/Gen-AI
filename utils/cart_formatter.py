def format_cart(cart, total):

    if not cart:

        return "Keranjang masih kosong."

    answer = "🛒 Keranjang Anda\n\n"

    for item in cart:

        answer += (
            f"• {item['name']} "
            f"x{item['quantity']}\n"
        )

        answer += (
            f"  Rp{item['subtotal']:,}"
            .replace(",", ".")
            + "\n\n"
        )

    answer += (
        "--------------------\n"
    )

    answer += (
        f"💰 Total: "
        f"Rp{total:,}"
        .replace(",", ".")
    )

    return answer