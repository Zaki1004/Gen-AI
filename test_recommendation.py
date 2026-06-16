from utils.preference_extractor import (
    extract_preferences
)

from services.recommendation_service import (
    recommend_by_preferences
)

from utils.recommendation_formatter import (
    format_recommendation
)

question = "Saya ingin kopi manis dingin"

preferences = extract_preferences(
    question
)

print("PREFERENCES:")
print(preferences)

result = recommend_by_preferences(
    preferences
)

print("\nRESULT:")
print(result)

print("\nANSWER:")
print(
    format_recommendation(result)
)