import pandas as pd

class WineRecommendation:
    def __init__(self):
        # Food and Wine Variety DataFrame
        self.food_wine_df = pd.DataFrame({
            'food': ['beef', 'chicken', 'chicken', 'chicken'],
            'wine_variety_id': [1, 2, 3, 4]
        })

        # Wine Variety DataFrame
        self.wine_variety_df = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'wine_variety': ['Cabernet Sauvignon', 'Chardonnay', 'Pinot Noir', 'Sauvignon Blanc']
        })

        # Brand DataFrame
        self.brand_df = pd.DataFrame({
            'id': list(range(1, 17)),
            'brand': ['Robert Mondavi', 'Silver Oak', 'Caymus', 'Beringer', 
                      'Kendall-Jackson', 'La Crema', 'Sonoma-Cutrer', 'Cakebread Cellars', 
                      'Bouchard Aîné & Fils', 'Louis Latour', 'Joseph Drouhin', 'Domaine Faiveley', 
                      'Kim Crawford', 'Cloudy Bay', 'Oyster Bay', 'Whitehaven']
        })

        # Wine Variety and Brand Relation DataFrame
        self.wine_brand_relation_df = pd.DataFrame({
            'wine_variety_id': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
            'brand_id': list(range(1, 17))
        })

    def recommend_based_on_food_and_brand(self, food, preferred_brand=None):
        # Get wine variety IDs for the given food
        wine_variety_ids = self.food_wine_df[self.food_wine_df['food'] == food]['wine_variety_id'].tolist()

        # Get brand IDs for these wine varieties
        brand_ids = self.wine_brand_relation_df[self.wine_brand_relation_df['wine_variety_id'].isin(wine_variety_ids)]['brand_id'].tolist()

        # Filter by the preferred brand if given
        if preferred_brand:
            recommended_brands = self.brand_df[(self.brand_df['id'].isin(brand_ids)) & (self.brand_df['brand'] == preferred_brand)]
        else:
            recommended_brands = self.brand_df[self.brand_df['id'].isin(brand_ids)].groupby('id').apply(lambda x: x.sample(2)).reset_index(drop=True)
        
        recommended_brands['wine_variety'] = recommended_brands['id'].map(self.wine_brand_relation_df.set_index('brand_id')['wine_variety_id']).map(self.wine_variety_df.set_index('id')['wine_variety'])

        return recommended_brands[['wine_variety', 'brand']]

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
