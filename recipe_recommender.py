
# Dataset of recipes
recipes = {
    "Spaghetti Pomodoro": ["pasta", "tomatoes", "garlic", "olive oil"],
    "Chicken Fried Rice": ["chicken", "rice", "garlic", "soy sauce"],
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Vegetable Stir-Fry": ["broccoli", "carrots", "soy sauce", "garlic", "ginger"],
    "Caprese Salad": ["tomatoes", "mozzarella", "basil", "olive oil", "balsamic vinegar"],
    "Banana Smoothie": ["banana", "milk", "yogurt", "honey", "ice"],
}


# Function to recommend recipes
def recommend_recipes(user_ingredients):
    recommendations = []
    user_ingredients = [ingredient.lower().strip() for ingredient in user_ingredients]
    for recipe, ingredients in recipes.items():
        common = set(user_ingredients).intersection(ingredients)
        missing = set(ingredients) - set(user_ingredients)
        if len(common) == len(ingredients):  # Exact match
            recommendations.append(f"You can make {recipe}!")
        elif len(common) / len(ingredients) >= 0.75:  # Partial match
            recommendations.append(f"You are close to making {recipe}! Missing: {', '.join(missing)}.")
    return recommendations if recommendations else ["No recipes match. Try adding more ingredients."]

# Input and output
print("Welcome to the Recipe Recommender!")
user_input = input("Enter your ingredients (comma-separated): ").split(",")
recommendations = recommend_recipes(user_input)
for rec in recommendations:
    print(rec)