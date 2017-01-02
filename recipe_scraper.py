import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


def mainprocess():
    recipes_list = {'Category':[], 'Recipe_Name':[], 'Link':[], 'Ingredients':[], 'Directions':[]}
    rootsite = r'http://www.vegweb.com'
    mainsite = rootsite + r'/recipes/'
    best_recipes_first = r'?sort_by=field_user_reviews_rating&sort_order=DESC'
    soup = get_site_text(mainsite)
    links = {cat.text.strip('\n').strip(): cat.a.get('href') for cat in soup.select('.views-row-content')}

    for category, url in links.items():
        recipe = {}
        soup = get_site_text(rootsite + url + best_recipes_first)
        recipe_links = {recipe.a.text.strip(): recipe.a.get('href') for recipe in soup.select('.group-middle')}
        for name, link in recipe_links.items():
            try:
                recipe_page = get_site_text(rootsite+link)
                recipe['Category'] = category
                recipe['Recipe_Name'] = name
                recipe['Link'] = rootsite + link
                recipe['Ingredients'] = recipe_page.select('p')[0].text
                recipe['Directions'] = recipe_page.select('p')[1].text.replace('[b]','').replace('[/b]','')
                [recipes_list[item].append(recipe[item]) for item in recipe]
                print('Finished {}'.format(name))
            except Exception as e:
                print('Error. {}'.format(e))

        print('***Done adding recipes from {}***'.format(category))
        
    df = pd.DataFrame(recipes_list)    
    df.to_json('recipes.json')

def get_site_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

if __name__ == '__main__':
    mainprocess()