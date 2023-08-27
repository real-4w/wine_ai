def recommend_wine_based_on_food(food):
    # A basic mapping of food to wine variety. This can be expanded.
    wine_recommendations = {
        'beef': 'Cabernet Sauvignon',
        'chicken': 'Chardonnay',
        'fish': 'Pinot Grigio',
        'lamb': 'Merlot',
        'pork': 'Shiraz',
        'vegetarian': 'Sauvignon Blanc'
    }
    
    return wine_recommendations.get(food.lower(), 'Pinot Noir')  # Default to Pinot Noir if food is not in our list

def virtual_sommelier():
    print("Welcome to the Virtual Sommelier!")
    food = input("What food are you eating? (e.g., beef, chicken, fish): ")
    
    recommended_wine = recommend_wine_based_on_food(food)
    
    print(f"For {food}, I recommend {recommended_wine}.")

virtual_sommelier()
