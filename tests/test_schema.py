from database.db_service import execute_query

print("ORDERS")
print(
    execute_query(
        "PRAGMA table_info(orders)"
    )
)

print()

print("ORDER ITEMS")
print(
    execute_query(
        "PRAGMA table_info(order_items)"
    )
)