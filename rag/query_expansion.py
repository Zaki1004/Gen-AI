EXPANSION_RULES = {

    "apa itu": [
        "pengertian",
        "definisi",
        "arti"
    ],

    "roasting": [
        "proses roasting",
        "teknik roasting",
        "pemanggangan kopi",
    ],

    "espresso": [
        "kopi espresso",
        "single shot espresso"
    ],

    "arabika": [
        "kopi arabika"
    ],

    "robusta": [
        "kopi robusta"
    ],

    "maillard": [
        "reaksi maillard"
    ],

    "cooling tray": [
        "pendinginan kopi",
        "cooling agitator"
    ]

}


def expand_query(question):

    question = question.lower()

    expanded = [question]

    for keyword, synonyms in EXPANSION_RULES.items():

        if keyword in question:

            expanded.extend(synonyms)

    return " ".join(expanded)