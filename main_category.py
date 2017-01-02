import pandas as pd
import re


def get_main_category(category):
    main_dict = {'Dinner':['Beans & Legumes', 'Burritos & Enchiladas', 'Casseroles', 'Dinner Pies',
                           'Global Cuisine', 'Pasta', 'Pizza', 'Rice & Grains', 'Sandwiches',
                           'Soups & Stews', 'Stir-Fries', 'Tofu, Tempeh, & Seitan', 'Vegetables',
                           'Slow Cooker', 'Meat & Dairy Alternatives', 'Raw Food'],
                 'Brunch':['Brunch'],
                 'Salad':['Salads'],
                 'Soup':['Soups & Stews'],
                 'Dessert':['Desserts'],
                 'Appetizer':['Snacks', 'Appetizers', 'Breads'],
                 'Other':['Non-Food Recipes', 'Holidays & Events', 'Kid-Friendly',
                          'Dips & Dressings', 'Cookbook Recipes', 'Beverages']}

    for key, values in main_dict.items():
        if category in values:
            return key

def setup_df():
    columns = ['Category', 'Recipe_Name', 'Link', 'Ingredients', 'Directions']
    df = pd.read_json('recipes.json')
    df = df[columns]
    df['Main_Category'] = df['Category'].apply(get_main_category)
    return df


if __name__ == '__main__':
    df = setup_df()
    df.to_json('recipes.json')