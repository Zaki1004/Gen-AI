from database.db_service import execute_query
from utils.query_normalizer import normalize_question
from config.ai_client import (
    get_gemini_client
)

from config.ai_model import (
    GEMINI_MODEL
)

def get_client():

    client = get_gemini_client()

    if not client:
        raise ValueError(
            "GEMINI_API_KEY tidak ditemukan."
        )

    return client

PROMPT_TEMPLATE = """
Anda adalah SQL Generator untuk Coffee Shop.

Database:

categories

1 = Coffee
2 = Non Coffee
3 = Snack
4 = Heavy Meal

Contoh:

Pertanyaan:
Menu kopi termurah apa?

SQL:
SELECT
    name,
    price
FROM menu_items
WHERE category_id = 1
ORDER BY price ASC
LIMIT 1;

Pertanyaan:
Menu kopi termahal apa?

SQL:
SELECT
    name,
    price
FROM menu_items
WHERE category_id = 1
ORDER BY price DESC
LIMIT 1;

Pertanyaan:
5 menu terlaris apa?

SQL:
SELECT
    m.name,
    mp.total_order
FROM menu_items m
JOIN menu_popularity mp
ON m.id = mp.menu_id
ORDER BY mp.total_order DESC
LIMIT 5;

menu_items
id
name
category_id
price
rating
stock
calories
caffeine_level
sweetness_level
serving_type
description
is_recommended

menu_popularity

menu_id
total_order
total_view

Rules:

- Untuk pertanyaan rekomendasi menu, harga termurah, harga termahal, rating tertinggi, selalu tampilkan:
  name, price, rating, description
- Output SQL saja
- Jangan gunakan markdown

Pertanyaan:
{question}
"""

def clean_sql(sql):

    sql = sql.replace(
        "```sql",
        ""
    )

    sql = sql.replace(
        "```",
        ""
    )

    return sql.strip()

def validate_sql(sql):

    forbidden = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE"
    ]

    sql_upper = sql.upper()

    for keyword in forbidden:

        if keyword in sql_upper:

            raise Exception(
                f"Forbidden SQL: {keyword}"
            )

    return True

def improve_sql(sql, question):

    question = question.lower()

    keywords = [
        "termurah",
        "termahal",
        "harga",
        "murah",
        "mahal"
    ]

    if any(word in question for word in keywords):

        if "price" not in sql.lower():

            sql = sql.replace(
                "SELECT name",
                "SELECT name, price"
            )

    return sql

def generate_sql(question):

    question = normalize_question(
        question
    )

    prompt = PROMPT_TEMPLATE.format(
        question=question
    )

    client = get_client()

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            # "temperature": 0,
            "max_output_tokens": 1024
        }
    )   

    sql = response.text

    sql = improve_sql(
    sql,
    question)

    validate_sql(sql)

    return sql

def generate_answer(
    question,
    result
):

    prompt = f"""
Anda adalah BaristaBot.

Pertanyaan User:
{question}

Data Hasil Query:
{result.to_string(index=False)}

Rules:

- Jawab dalam Bahasa Indonesia.
- Jangan mengarang data.
- Gunakan hanya data yang tersedia.
- Jika ada harga tampilkan format Rp.
- Jika ada rating tampilkan simbol ⭐.
- Buat jawaban ringkas dan profesional.
- Gunakan format poin.

"""

    client = get_client()

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            # "temperature": 0.1,
            "max_output_tokens": 1024
        }  
    )

    return response.text

def ask_database(question):

    sql = generate_sql(question)

    print("\nSQL:")
    print(sql)

    result = execute_query(sql)

    print("\nRESULT:")
    print(result)

    answer = generate_answer(
        question,
        result
    )

    return answer