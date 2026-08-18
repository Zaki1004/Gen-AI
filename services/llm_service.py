from config.ai_client import (
    get_gemini_client
)

from config.ai_model import (
    GEMINI_MODEL
)

client = get_gemini_client()

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

    contents = []

    for message in messages:

        contents.append(
            {
                "role": message["role"],
                "parts": [
                    {
                        "text": message["content"]
                    }
                ]
            }
        )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=contents,
        config={
            "system_instruction": SYSTEM_PROMPT,
            # "temperature": 0.1,
            "max_output_tokens": 1024
        }
    )

    return response.text