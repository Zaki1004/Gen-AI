from tools.sql_tool import text_to_sql, run_sql, sql_to_answer

question = "Menu kopi termurah apa?"

sql = text_to_sql(question)
print("SQL:", sql)

result = run_sql(sql)
print("\nRESULT:\n", result)

answer = sql_to_answer(question, result)
print("\nANSWER:\n", answer)