from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "coffee.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ==========================
# Categories
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
)
""")

# ==========================
# Menu Items
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    category_id INTEGER NOT NULL,

    price INTEGER NOT NULL,

    rating REAL DEFAULT 0,

    stock INTEGER DEFAULT 100,

    calories INTEGER,

    caffeine_level TEXT,

    sweetness_level TEXT,

    serving_type TEXT,

    image_path TEXT,

    description TEXT,

    is_recommended INTEGER DEFAULT 0,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(category_id)
    REFERENCES categories(id)
)
""")

# ==========================
# Menu Tags
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    menu_id INTEGER NOT NULL,

    tag TEXT NOT NULL,

    FOREIGN KEY(menu_id)
    REFERENCES menu_items(id)
)
""")

# ==========================
# Users
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# ==========================
# Orders
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    total_price INTEGER DEFAULT 0,

    order_status TEXT DEFAULT 'pending',

    payment_status TEXT DEFAULT 'unpaid',

    payment_token TEXT,

    payment_method TEXT,

    qr_code TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
)
""")

# ==========================
# Order Items
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    order_id INTEGER NOT NULL,

    menu_id INTEGER NOT NULL,

    quantity INTEGER DEFAULT 1,

    subtotal INTEGER NOT NULL,

    notes TEXT,

    FOREIGN KEY(order_id)
    REFERENCES orders(id),

    FOREIGN KEY(menu_id)
    REFERENCES menu_items(id)
)
""")

# ==========================
# Popularity
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_popularity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    menu_id INTEGER,

    total_order INTEGER DEFAULT 0,

    total_view INTEGER DEFAULT 0,

    FOREIGN KEY(menu_id)
    REFERENCES menu_items(id)
)
""")

conn.commit()
conn.close()

print("Database berhasil dibuat!")