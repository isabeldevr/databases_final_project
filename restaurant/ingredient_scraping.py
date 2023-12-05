import requests
import os
from dotenv import load_dotenv
import json
import traceback


def get_ingredients(food_name):
     """Get ingredients from API callbased on food name.
     Args:
          food_name ([str]): [name of food]
     Returns:
          [list]: [list of ingredients] """
     try:
          url = "https://api.edamam.com/api/recipes/v2"

          params = {
               "type": "public",
               "q": food_name,
               "app_id": "d1e22f44",
               "app_key": "902a662f52555a094e6aaa17e0e47a37", 
          }

          response = requests.get(url, params=params)

          if response.status_code == 200:
               data = response.json()
               hits = data.get("hits", [])
               if hits:
                    first_recipe = hits[0]["recipe"]
                    return first_recipe.get("ingredientLines", [])
          return []
     except Exception as e:
          print("Error getting ingredients. 'Returning empty list.'Make sure that the key is working before continuing.")
          print(e)
          traceback.print_exc()
          return []



def get_menu_items():
     """This function returns a list of menu items.
     Returns:
          [list]: [list of menu items]"""
     menu_items = [
          'Nigiri Salmon',
          'Nigiri Tuna',
          'Nigiri Ebi',
          'Nigiri Avocado',
          'Sake Mango',
          'Tartar White',
          'Salmon Roll',
          'Green Dragon Roll',
          'Philadelphia Roll',
          'Surimi Roll',
          'Crab Roll',
          'Surimi Thin Roll',
          'Tuna Thin Roll',
          'Avocado Thin Roll',
          'Salmon Thin Roll',
          'Salmon Temaki',
          'Shrimp Temaki',
          'Spicy Temaki',
          'Lemon Tori',
          'Spicy Tori',
          'Koroke',
          'Breaded Shrimp',
          'Breaded Calamar',
          'Spring Rolls',
          'Uramaki',
     ] 
     return menu_items


def save_to_json(menu_items, json_file):
     """Save menu items to json file.
     Args:
          menu_items ([list]): [list of menu items]
          json_file ([str]): [name of json file]
     Returns:
          [type]: [description]"""
     try: 
          with open(json_file, 'w') as file:
               json.dump(menu_items, file, indent=2)
     except Exception as e:
          print("Error saving to json file.")
          print(e)
          traceback.print_exc()


def main():
    menu_items = {a: None for a in get_menu_items()}

    for food_name in menu_items:
          print(f"Food Name: {food_name}")
          ingredients = get_ingredients(food_name)
          if ingredients:
               for ingredient in ingredients:
                     print("-", ingredient)
               menu_items[food_name] = ingredients
          else:
               print("No ingredients found.")
               print("\n")

main()