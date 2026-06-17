from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = (
    BASE_DIR /
    "database" /
    "coffee.db"
)


def pay_order(payment_token):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE orders
    SET
        payment_status = 'paid'
    WHERE payment_token = ?
    """, (
        payment_token,
    ))

    conn.commit()

    updated_rows = cursor.rowcount

    conn.close()

    return updated_rows > 0


def get_order(payment_token):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        payment_status,
        total_price
    FROM orders
    WHERE payment_token = ?
    """, (
        payment_token,
    ))

    result = cursor.fetchone()

    conn.close()

    return result