lists = [
    {"fruits": "apple", "calories": "130"},
    {"fruits": "avocado", "calories": "50"},
    {"fruits": "banana", "calories": "110"},
    {"fruits": "canteloupe", "calories": "50"},
    {"fruits": "grapefruit", "calories": "60"},
    {"fruits": "grapes", "calories": "90"},
    {"fruits": "honeydew melon", "calories": "50"},
    {"fruits": "kiwifruit", "calories": "90"},
    {"fruits": "lemon", "calories": "15"},
    {"fruits": "lime", "calories": "20"},
    {"fruits": "nectarine", "calories": "60"},
    {"fruits": "orange", "calories": "80"},
    {"fruits": "peach", "calories": "60"},
    {"fruits": "pear", "calories": "100"},
    {"fruits": "pineapple", "calories": "50"},
    {"fruits": "plums", "calories": "70"},
    {"fruits": "strawberries", "calories": "50"},
    {"fruits": "sweet cherries", "calories": "100"},
    {"fruits": "tangerine", "calories": "50"},
    {"fruits": "watermelon", "calories": "80"},
]

nutrition=input("Item: ").strip().lower()
for i in lists:
    if i["fruits"] in nutrition:
        print("Calories: ",i["calories"])