from config.ai_client import get_gemini_client
from config.ai_model import GEMINI_MODEL


client = get_gemini_client()

response = client.models.generate_content(
    model=GEMINI_MODEL,
    contents="Jawab Singkat: apa itu kopi?"
)

print(response.text)