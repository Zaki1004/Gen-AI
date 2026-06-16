def format_recommendation(df):

    text = "☕ Rekomendasi Menu\n\n"

    for _, row in df.iterrows():

        price = f"{row['price']:,}".replace(",", ".")

        text += f"""
Nama: {row['name']}
Harga: Rp{price}
Rating: ⭐ {row['rating']}
Deskripsi: {row['description']}

"""

    return text