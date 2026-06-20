from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = (
    BASE_DIR /
    "database" /
    "coffee.db"
)


def get_recent_orders():

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        total_price,
        payment_status
    FROM orders
    ORDER BY id DESC
    LIMIT 10
    """)

    result = cursor.fetchall()

    conn.close()

    return result