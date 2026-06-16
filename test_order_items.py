from database.db_service import execute_query

query = """
SELECT *
FROM order_items
"""

print(
    execute_query(query)
)