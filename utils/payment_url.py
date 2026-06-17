def generate_payment_url(
    payment_token
):

    return (
        f"http://localhost:8501/"
        f"?payment={payment_token}"
    )