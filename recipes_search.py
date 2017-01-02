import pandas as pd
import re
import random


def load_df():
    columns = ['Main_Category', 'Category', 'Recipe_Name', 'Link', 'Ingredients', 'Directions']
    df = pd.read_json('recipes.json')
    df = df[columns]
    return df


def recipe_search(df, category=None, ingredients=None):

    if category in df.Main_Category.unique():
        results = df.where(df.Main_Category.str.contains(category)).dropna()

    elif category in df.Category.unique():
        results = df.where(df.Category.str.contains(category)).dropna()

    if ingredients:
        ingredients = ingredients.replace('and', '').replace('or', '')
        ingredients = ingredients.split()
        for ingredient in ingredients:
            results_ingr = results.where(df.Ingredients.str.contains(ingredient)).dropna()
            if len(results_ingr) > 0:
                results = results_ingr
            else:
                print('{} was not found in combination with other ingredients!'.format(ingredient))



        selections = list({random.choice(results.index) for _ in range(10)})
        selections = selections[:min(len(selections), 3)]
        return df.iloc[selections]

if __name__ == '__main__':
    df = load_df()
    print(recipe_search(df, 'Dinner', 'tofu'))
