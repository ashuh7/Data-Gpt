from database import execute_query


query = """
SELECT *
FROM orders
LIMIT 5;
"""


result = execute_query(query)

print(result)