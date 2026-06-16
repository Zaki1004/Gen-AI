from tools.sql_tool import ask_database

question = "Menu kopi termurah apa?"

answer = ask_database(
    question
)

print("\nANSWER:")
print(answer)