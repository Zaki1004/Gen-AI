from services.llm_service import client
from database.db_service import execute_query


SYSTEM_PROMPT = """
Kamu adalah SQL Expert untuk database coffee shop.

Tabel:

menu_items:
- id
- name
- category_id
- price
- rating
- stock
- calories
- caffeine_level
- sweetness_level
- serving_type
- description
- is_recommended

categories:
- id
- name

Instruksi:
- Ubah pertanyaan user menjadi SQL query SQLite
- HANYA OUTPUT SQL SAJA
- Tidak boleh ada penjelasan
- Gunakan SELECT saja
"""


def text_to_sql(question: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    sql_query = response.choices[0].message.content
    return sql_query.strip()


def run_sql(query: str):
    try:
        result = execute_query(query)
        return result
    except Exception as e:
        return str(e)


def sql_to_answer(question: str, result):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Kamu adalah barista AI yang menjelaskan hasil query database secara natural"
            },
            {
                "role": "user",
                "content": f"""
Pertanyaan: {question}

Hasil database:
{result}

Jelaskan dalam bahasa Indonesia yang natural dan ramah.
"""
            }
        ]
    )

    return response.choices[0].message.content