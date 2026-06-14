from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
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