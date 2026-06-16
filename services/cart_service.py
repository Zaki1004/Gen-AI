from database.db_service import execute_query


def get_menu_price(menu_name):

    query = f"""
    SELECT
        id,
        name,
        price
    FROM menu_items
    WHERE LOWER(name) =
    LOWER('{menu_name}')
    """

    result = execute_query(query)

    return result


def build_cart(order_list):

    cart = []

    total_price = 0

    for item in order_list:

        menu = get_menu_price(
            item["menu_name"]
        )

        if menu.empty:
            continue

        price = int(
            menu.iloc[0]["price"]
        )

        subtotal = int(
            price *
            item["quantity"]
        )

        total_price += subtotal

        cart.append({
            "name": menu.iloc[0]["name"],
            "quantity": item["quantity"],
            "price": price,
            "subtotal": subtotal
        })

    return cart, total_price