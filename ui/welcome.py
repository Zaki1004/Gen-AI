import streamlit as st


def init_welcome():

    if "messages" not in st.session_state:

        st.session_state.messages = [

            {

                "role": "assistant",

                "content":

                (
                    "👋 Halo!\n\n"

                    "Selamat Datang di CoffeeBot.\n"

                    "Saya adalah AI Coffee Shop Assistant yang siap membantu Anda.\n\n"

                    "Saya dapat:\n\n"

                    "☕ Menjawab pertanyaan tentang kopi\n\n"

                    "📚 Menjelaskan tentang kopi\n\n"

                    "🍰 Memberikan rekomendasi\n\n"

                    "🛒 Melakukan pemesanan\n\n"

                    "Silakan bertanya 😊"

                )

            }

        ]