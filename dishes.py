dishes = {
    "butter_naan": "Wheat, curd, yeast",
    "chai": "Water, Milk, tea leaves, sugar, spices",
    "chapati": "Wheat flour, water",
    "chole_bhature": "Chickpeas, onion, tomato, flour, yogurt (curd)",
    "dal_makhani": "Urad dal or kali dal, rajma",
    "dhokla": "Flour (besan), baking soda, curry leaves",
    "fried_rice": "Cooked rice, vegetables",
    "idli": "Rice, fenugreek seeds, urad dal",
    "Jalebi": "Besan, sugar, baking soda, yogurt, flour, ghee",
    "Kaathi_rolls": "White flour, coriander chutney, egg, chicken",
    "kadai_paneer": "Paneer, Onion, Tomatoes, Capsicum",
    "kulfi": "Milk, sugar",
    "masala_dosa": "Rice, black lentils, potatoes, onions, spices",
    "momos": "Flour, vegetables, chicken, paneer",
    "paani_puri": "Potatoes, chickpeas, spiced water, onions, sev",
    "pakoda": "Veggies, besan"
}

# Prompt the user to input a dish name
dish_name = input("Enter the name of the dish: ")

# Convert input to lowercase for case-insensitive matching
dish_name = dish_name.lower()

# Check if the dish exists in the dictionary
if dish_name in dishes:
    # If the dish exists, print its ingredients
    print("Ingredients for", dish_name + ":", dishes[dish_name])
else:
    # If the dish doesn't exist, print an error message
    print("Dish not found!")
    dishes = {
    "butter_naan": "Wheat, curd, yeast",
    "chai": "Water, Milk, tea leaves, sugar, spices",
    "chapati": "Wheat flour, water",
    "chole_bhature": "Chickpeas, onion, tomato, flour, yogurt (curd)",
    "dal_makhani": "Urad dal or kali dal, rajma",
    "dhokla": "Flour (besan), baking soda, curry leaves",
    "fried_rice": "Cooked rice, vegetables",
    "idli": "Rice, fenugreek seeds, urad dal",
    "Jalebi": "Besan, sugar, baking soda, yogurt, flour, ghee",
    "Kaathi_rolls": "White flour, coriander chutney, egg, chicken",
    "kadai_paneer": "Paneer, Onion, Tomatoes, Capsicum",
    "kulfi": "Milk, sugar",
    "masala_dosa": "Rice, black lentils, potatoes, onions, spices",
    "momos": "Flour, vegetables, chicken, paneer",
    "paani_puri": "Potatoes, chickpeas, spiced water, onions, sev",
    "pakoda": "Veggies, besan"
}

# Prompt the user to input a dish name
dish_name = input("Enter the name of the dish: ")

# Convert input to lowercase for case-insensitive matching
dish_name = dish_name.lower()

# Check if the dish exists in the dictionary
if dish_name in dishes:
    # If the dish exists, print its ingredients
    print("Ingredients for", dish_name + ":", dishes[dish_name])
else:
    # If the dish doesn't exist, print an error message
    print("Dish not found!")