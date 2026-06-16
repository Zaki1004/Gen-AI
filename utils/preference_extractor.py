import re

def extract_preferences(question):

    question = question.lower()

    preferences = {}

    # ======================
    # CATEGORY
    # ======================

    if "kopi" in question:
        preferences["category_id"] = 1

    elif "non coffee" in question:
        preferences["category_id"] = 2

    elif "snack" in question:
        preferences["category_id"] = 3

    elif "makanan berat" in question:
        preferences["category_id"] = 4

    # ======================
    # SWEETNESS
    # ======================

    if "sangat manis" in question:
        preferences["sweetness_level"] = "High"

    elif "manis" in question:
        preferences["sweetness_level"] = "High"

    elif "sedang" in question:
        preferences["sweetness_level"] = "Medium"

    elif "tidak terlalu manis" in question:
        preferences["sweetness_level"] = "Low"

    # ======================
    # SERVING TYPE
    # ======================

    if "dingin" in question:
        preferences["serving_type"] = "Cold"

    elif "panas" in question:
        preferences["serving_type"] = "Hot"

    # ======================
    # CAFFEINE
    # ======================

    if "kopi kuat" in question:
        preferences["caffeine_level"] = "Very High"

    elif "strong coffee" in question:
        preferences["caffeine_level"] = "Very High"

    elif "kafein tinggi" in question:
        preferences["caffeine_level"] = "High"

    elif "kafein sedang" in question:
        preferences["caffeine_level"] = "Medium"

    elif "kafein rendah" in question:
        preferences["caffeine_level"] = "Low"

    elif "tanpa kafein" in question:
        preferences["caffeine_level"] = "None"

    # ======================
    # DIET
    # ======================

    if "diet" in question:
        preferences["low_calorie"] = True

    # ======================
    # RECOMMENDED
    # ======================

    recommended_keywords = [
        "rekomendasi",
        "best seller",
        "favorit",
        "menu favorit",
        "recommended"
    ]

    if any(word in question for word in recommended_keywords):
        preferences["is_recommended"] = 1

    # ======================
    # RATING
    # ======================

    rating_keywords = [
        "terbaik",
        "rating tinggi",
        "paling enak"
    ]

    if any(word in question for word in rating_keywords):
        preferences["min_rating"] = 4.7

    # ======================
    # BUDGET
    # ======================

    match = re.search(r'(\d+)\s*ribu', question)

    if match:

        budget = int(match.group(1)) * 1000

        preferences["max_price"] = budget

    return preferences