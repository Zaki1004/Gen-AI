cart = []


def add_to_cart(item):

    global cart

    for existing in cart:

        if existing["name"] == item["name"]:

            existing["quantity"] += item["quantity"]

            existing["subtotal"] += item["subtotal"]

            return

    cart.append(item)


def get_cart():

    return cart


def clear_cart():

    global cart

    cart.clear()


def get_total():

    total = 0

    for item in cart:

        total += item["subtotal"]

    return total


def remove_from_cart(menu_name):

    global cart

    cart = [

        item

        for item in cart

        if item["name"].lower()
        != menu_name.lower()

    ]