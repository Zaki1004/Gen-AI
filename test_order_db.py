from database.db_service import execute_query

query = """
SELECT *
FROM orders
"""

print(
    execute_query(query)
)