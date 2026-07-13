from database.db_service import execute_query

query = """
SELECT
    name,
    price
FROM menu_items
ORDER BY price ASC
"""

result = execute_query(query)

print(result)