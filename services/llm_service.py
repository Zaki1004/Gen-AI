from config.ai_client import (
    get_groq_client
)

from config.ai_model import (
    GROQ_MODEL
)

client = get_groq_client()

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

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        temperature=0.3,
        max_tokens=1024,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + messages
    )

    return response.choices[0].message.content