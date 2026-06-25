from utils.preference_extractor import (
    extract_preferences
)

from services.recommendation_service import (
    recommend_by_preferences
)

from utils.recommendation_formatter import (
    format_recommendation
)


def recommendation_tool_node(
    question
):

    preferences = extract_preferences(
        question
    )

    results = recommend_by_preferences(
        preferences
    )

    return format_recommendation(
        results
    )