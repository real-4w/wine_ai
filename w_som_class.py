import pandas as pd

class WineRecommendation:
    def __init__(self):
        # Food and Wine DataFrame
        self.food_wine_df = pd.DataFrame({
            'food': ['beef', 'chicken', 'chicken', 'chicken'],
            'wine_variety': ['Cabernet Sauvignon', 'Chardonnay', 'Pinot Noir', 'Sauvignon Blanc']
        })

        # Wine and Brand DataFrame
        self.wine_brand_df = pd.DataFrame({
            'wine_variety': ['Cabernet Sauvignon', 'Merlot', 'Shiraz', 'Chardonnay', 'Pinot Noir', 'Sauvignon Blanc', 'Riesling'],
            'brand': ['Robert Mondavi', 'Barefoot', 'Penfolds', 'Kendall-Jackson', 'Bouchard Aîné & Fils', 'Kim Crawford', 'Chateau Ste. Michelle']
        })

    def recommend_based_on_food_and_brand(self, food, preferred_brand=None):
        # First, get the wine varieties for the food
        wine_varieties = self.food_wine_df[self.food_wine_df['food'] == food]['wine_variety'].tolist()

        # Then, filter wine brands by those varieties and, optionally, by the preferred brand
        if preferred_brand:
            recommended_brands = self.wine_brand_df[(self.wine_brand_df['wine_variety'].isin(wine_varieties)) & (self.wine_brand_df['brand'] == preferred_brand)]
        else:
            recommended_brands = self.wine_brand_df[self.wine_brand_df['wine_variety'].isin(wine_varieties)]
        
        return recommended_brands

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
