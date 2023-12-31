import pandas as pd
import random

class VirtualSommelier:
    def __init__(self):
        # Setting up the multi-index DataFrame
        data = {
            ('Cabernet Sauvignon', 'Robert Mondavi'): {'description': 'Rich and flavorful'},
            ('Cabernet Sauvignon', 'Silver Oak'): {'description': 'Bold and spicy'},
            ('Cabernet Sauvignon', 'Caymus'): {'description': 'Smooth and velvety'},
            ('Cabernet Sauvignon', 'Beringer'): {'description': 'Bright and crisp'},
            ('Chardonnay', 'Kendall-Jackson'): {'description': 'Buttery and oaky'},
            ('Chardonnay', 'La Crema'): {'description': 'Fresh and zesty'},
            ('Chardonnay', 'Sonoma-Cutrer'): {'description': 'Rich and full-bodied'},
            ('Chardonnay', 'Cakebread Cellars'): {'description': 'Mineral-driven'},
            ('Pinot Noir', 'Bouchard Aîné & Fils'): {'description': 'Elegant and refined'},
            ('Pinot Noir', 'Louis Latour'): {'description': 'Berry-rich'},
            ('Pinot Noir', 'Joseph Drouhin'): {'description': 'Earthy tones'},
            ('Pinot Noir', 'Domaine Faiveley'): {'description': 'Robust and lingering'},
            ('Sauvignon Blanc', 'Kim Crawford'): {'description': 'Zesty and tropical'},
            ('Sauvignon Blanc', 'Cloudy Bay'): {'description': 'Crisp and aromatic'},
            ('Sauvignon Blanc', 'Oyster Bay'): {'description': 'Lush and balanced'},
            ('Sauvignon Blanc', 'Whitehaven'): {'description': 'Bright and fruity'}
        }
        self.wine_data_df = pd.DataFrame(data).T

    def recommend_wines(self, food, favorite_brands):
        # Mapping food to wine varieties
        food_wine_map = {
            'beef': 'Cabernet Sauvignon',
            'chicken': 'Chardonnay',
            'pork': 'Pinot Noir',
            'fish': 'Sauvignon Blanc'
        }
        
        wine_variety = food_wine_map.get(food)
        if not wine_variety:
            print("Sorry, I don't have a recommendation for that food.")
            return
        
        brands_for_variety = self.wine_data_df.loc[wine_variety].index.tolist()
        
        # Prioritize favorite brands in the recommendations
        prioritized_brands = [brand for brand in favorite_brands if brand in brands_for_variety]
        
        # If fewer than 2 favorite brands are suitable, fill in with other brands
        while len(prioritized_brands) < 2:
            brand = random.choice(brands_for_variety)
            if brand not in prioritized_brands:
                prioritized_brands.append(brand)

        recommendations = []
        for brand in prioritized_brands:
            description = self.wine_data_df.loc[(wine_variety, brand), 'description']
            recommendations.append((wine_variety, brand, description))
        
        return recommendations
    
    def interact_with_user(self):
        print("Welcome to the Virtual Sommelier!")
        
        # Get favorite brands
        favorite_brands_input = input("What are some of your favorite wine brands? (Separate them by commas): ")
        favorite_brands = [brand.strip() for brand in favorite_brands_input.split(",")]
        
        food = input("What food are you eating? (e.g., beef, chicken): ")
        
        recommended_wines = self.recommend_wines(food, favorite_brands)
        if recommended_wines:
            print(f"\nFor {food}, I recommend:")
            for wine_variety, brand, description in recommended_wines:
                print(f"- {wine_variety} from {brand}: {description}")
        print("\nEnjoy your meal and wine pairing!")

if __name__ == "__main__":
    sommelier = VirtualSommelier()
    sommelier.interact_with_user()
