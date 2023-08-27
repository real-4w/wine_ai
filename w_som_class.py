import pandas as pd

class WineRecommendation:
    def __init__(self):
        # Create a DataFrame with food, wine variety, and brands
        data = {
            'food': ['beef', 'beef', 'beef', 'chicken', 'chicken', 'chicken'],
            'wine_variety': ['Cabernet Sauvignon', 'Merlot', 'Shiraz', 'Chardonnay', 'Pinot Noir', 'Sauvignon Blanc'],
            'brand': ['Brand A', 'Brand C', 'Brand E', 'Brand G', 'Brand I', 'Brand K']
        }
        
        self.df = pd.DataFrame(data)

    def recommend_based_on_food_and_brand(self, food, preferred_brand=None):
        # Filter DataFrame by food and, optionally, by brand
        filtered_df = self.df[self.df['food'] == food]
        
        if preferred_brand:
            filtered_df = filtered_df[filtered_df['brand'] == preferred_brand]
        
        return filtered_df

class VirtualSommelier:
    def __init__(self):
        self.wine_recommender = WineRecommendation()

    def interact_with_user(self):
        print("Welcome to the Virtual Sommelier!")
        food = input("What food are you eating? (e.g., beef, chicken): ")
        preferred_brand = input("Do you have a preferred wine brand? (Leave blank for any): ")

        recommended_wines = self.wine_recommender.recommend_based_on_food_and_brand(food, preferred_brand)
        print(f"For {food}, I recommend:")
        
        for _, row in recommended_wines.iterrows():
            print(f"- {row['wine_variety']} from brand: {row['brand']}")


if __name__ == "__main__":
    sommelier = VirtualSommelier()
    sommelier.interact_with_user()

