import secrets


def generate_payment_token():

    return secrets.token_urlsafe(16)