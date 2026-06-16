CATEGORY_MAPPING = {
    "coffee": 1,
    "kopi": 1,

    "non coffee": 2,
    "non kopi": 2,

    "snack": 3,

    "heavy meal": 4,
    "makanan berat": 4
}

TABLE_DESCRIPTION = """
categories
---------
id
name
description

menu_items
----------
id
name
category_id
price
rating
stock
calories
caffeine_level
sweetness_level
serving_type
description
is_recommended

menu_popularity
---------------
id
menu_id
total_order
total_view
"""