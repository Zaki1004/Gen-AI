from pathlib import Path
import sqlite3

from utils.token_generator import (
    generate_payment_token
)

from services.qr_service import (
    generate_qr
)

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = (
    BASE_DIR /
    "database" /
    "coffee.db"
)


def create_order(total_price):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    payment_token = (
        generate_payment_token()
    )

    cursor.execute("""
    INSERT INTO orders (
        total_price,
        order_status,
        payment_status,
        payment_token
    )
    VALUES (?, ?, ?, ?)
    """, (
        int(total_price),
        "pending",
        "unpaid",
        payment_token
    ))

    order_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return (
        order_id,
        payment_token
    )


def create_order_items(
    order_id,
    cart
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    for item in cart:

        cursor.execute("""
        SELECT id
        FROM menu_items
        WHERE name = ?
        """, (
            item["name"],
        ))

        menu = cursor.fetchone()

        if not menu:
            continue

        menu_id = menu[0]

        cursor.execute("""
        INSERT INTO order_items (
            order_id,
            menu_id,
            quantity,
            subtotal
        )
        VALUES (?, ?, ?, ?)
        """, (
            int(order_id),
            int(menu_id),
            int(item["quantity"]),
            int(item["subtotal"])
        ))

    conn.commit()
    conn.close()


def generate_order_number(order_id):

    return f"ORD-{order_id:05d}"


def checkout(
    cart,
    total_price
):

    order_id, payment_token = (
        create_order(total_price)
    )

    create_order_items(
        order_id,
        cart
    )

    order_number = (
        generate_order_number(
            order_id
        )
    )

    qr_path = (
        generate_qr(
            order_number
        )
    )

    return {
        "order_id": order_id,
        "order_number": order_number,
        "payment_token": payment_token,
        "qr_path": qr_path
    }