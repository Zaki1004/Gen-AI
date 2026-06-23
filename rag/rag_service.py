from groq import Groq
from dotenv import load_dotenv

from rag.retriever import (
    retrieve_context
)

import os

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


RAG_SYSTEM_PROMPT = """
Kamu adalah Coffee Expert Assistant.

Gunakan hanya informasi yang tersedia
pada context.

Jika context tidak memiliki jawaban,
katakan bahwa informasi tidak ditemukan
di knowledge base.

Jawab dalam Bahasa Indonesia.

Jangan mengarang.
"""


def ask_rag(
    question
):

    retrieved_docs = (
        retrieve_context(
            question
        )
    )

    context = "\n\n".join(
        [
            doc["content"]
            for doc in retrieved_docs
        ]
    )

    print(
        "\n===== CONTEXT =====\n"
    )

    print(
        context[:5000]
    )

    prompt = f"""
Context:

{context}

Question:

{question}
"""

    response = (
        client.chat.completions.create(
            model=
            "llama-3.3-70b-versatile",

            temperature=0,

            messages=[
                {
                    "role":
                    "system",

                    "content":
                    RAG_SYSTEM_PROMPT
                },
                {
                    "role":
                    "user",

                    "content":
                    prompt
                }
            ]
        )
    )

    return (
        response
        .choices[0]
        .message
        .content
    )