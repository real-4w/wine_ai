class WineRecommendation:
    def __init__(self):
        # An expanded mapping of food to wine variety. 
        self.wine_recommendations = {
            'beef': ['Cabernet Sauvignon', 'Merlot', 'Shiraz'],
            'chicken': ['Chardonnay', 'Pinot Noir', 'Sauvignon Blanc'],
            'grilled fish': ['Pinot Grigio', 'Chardonnay'],
            'spicy fish': ['Riesling', 'Gewürztraminer'],
            'lamb': ['Merlot', 'Zinfandel', 'Cabernet Franc'],
            'pork': ['Shiraz', 'Tempranillo', 'Pinot Noir'],
            'spicy food': ['Syrah', 'Grenache', 'Viognier'],
            'vegetarian': ['Sauvignon Blanc', 'Pinot Grigio', 'Chenin Blanc'],
            'cheese': ['Chardonnay', 'Riesling', 'Cabernet Sauvignon'],
            'chocolate dessert': ['Port', 'Sherry', 'Merlot'],
            'fruity dessert': ['Moscato', 'Sauternes', 'Riesling']
        }

    def recommend_based_on_food(self, food):
        # Return a list of recommendations or default to ['Pinot Noir', 'Merlot', 'Cabernet Sauvignon']
        return self.wine_recommendations.get(food.lower(), ['Pinot Noir', 'Merlot', 'Cabernet Sauvignon'])


class VirtualSommelier:
    def __init__(self):
        self.wine_recommender = WineRecommendation()

    def interact_with_user(self):
        print("Welcome to the Virtual Sommelier!")
        food = input("What food are you eating? (e.g., beef, chicken, spicy fish, chocolate dessert): ")

        recommended_wines = self.wine_recommender.recommend_based_on_food(food)
        print(f"For {food}, I recommend:")
        for wine in recommended_wines:
            print(f"- {wine}")


if __name__ == "__main__":
    sommelier = VirtualSommelier()
    sommelier.interact_with_user()
