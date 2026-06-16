from database.db_service import execute_query

def recommend_by_preferences(preferences):

    query = """
    SELECT
        name,
        price,
        rating,
        description
    FROM menu_items
    WHERE 1=1
    """

    if "category_id" in preferences:

        query += f"""
        AND category_id =
        {preferences['category_id']}
        """

    if "sweetness_level" in preferences:

        query += f"""
        AND sweetness_level =
        '{preferences['sweetness_level']}'
        """

    if "caffeine_level" in preferences:

        query += f"""
        AND caffeine_level =
        '{preferences["caffeine_level"]}'
        """

    if "serving_type" in preferences:

        query += f"""
        AND serving_type =
        '{preferences['serving_type']}'
        """


    if "caffeine_level" in preferences:

        query += f"""
        AND caffeine_level =
        '{preferences["caffeine_level"]}'
        """


    if "max_price" in preferences:

        query += f"""
        AND price <=
        {preferences["max_price"]}
        """


    if "min_rating" in preferences:

        query += f"""
        AND rating >=
        {preferences["min_rating"]}
        """


    if "is_recommended" in preferences:

        query += """
        AND is_recommended = 1
        """

    if preferences.get("low_calorie"):

        query += """
        ORDER BY calories ASC
        LIMIT 5
        """

    else:

        query += """
        ORDER BY rating DESC
        LIMIT 5
        """

    return execute_query(query)
