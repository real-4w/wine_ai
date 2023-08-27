class WineRecommendation:
    def __init__(self):
        # A basic mapping of food to wine variety. This can be expanded.
        self.wine_recommendations = {
            'beef': 'Cabernet Sauvignon',
            'chicken': 'Chardonnay',
            'fish': 'Pinot Grigio',
            'lamb': 'Merlot',
            'pork': 'Shiraz',
            'vegetarian': 'Sauvignon Blanc'
        }

    def recommend_based_on_food(self, food):
        return self.wine_recommendations.get(food.lower(), 'Pinot Noir')  # Default to Pinot Noir if food is not in our list


class VirtualSommelier:
    def __init__(self):
        self.wine_recommender = WineRecommendation()

    def interact_with_user(self):
        print("Welcome to the Virtual Sommelier!")
        food = input("What food are you eating? (e.g., beef, chicken, fish): ")

        recommended_wine = self.wine_recommender.recommend_based_on_food(food)
        print(f"For {food}, I recommend {recommended_wine}.")


if __name__ == "__main__":
    sommelier = VirtualSommelier()
    sommelier.interact_with_user()
