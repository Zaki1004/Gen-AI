from config.ai_client import (
    get_groq_client
)

SYSTEM_PROMPT = """
Kamu adalah BaristaBot.

Kepribadian:
- Ramah
- Profesional
- Ahli kopi
- Menjawab dalam Bahasa Indonesia

Tugas:
- Menjelaskan kopi
- Memberikan rekomendasi kopi
- Membantu pelanggan coffee shop
- Menjelaskan menu secara sederhana

Jika tidak mengetahui informasi tertentu,
jawab dengan jujur dan jangan mengarang.
"""


def generate_response(messages):

    client = get_groq_client()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=1024,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + messages
    )

    return response.choices[0].message.content