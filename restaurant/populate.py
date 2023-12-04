import os
import django
from faker import Faker
import random
import pymongo
import json
import datetime
from decimal import Decimal, InvalidOperation
from pymongo import MongoClient
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import uuid
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')
django.setup()
# configure settings
# import models
from restaurant_app.models import MenuItem, IngredientType, MenuIngredient, Order, Payment


alergies = {'Shellfish', 'Peanut', 'Dairy', 'Wheat', 'Fish', 'Egg', 'Soy', 'Sesame', 'Gluten', 'Tree Nut'}

fake = Faker()


def get_menu():
     with open('../menu_items.json') as json_file:
          data = json.load(json_file)
          return data
     
def get_ingredients():
     menu = get_menu()
     ings = [a for a in menu.values()]
     # flatten
     ings = [item for sublist in ings for item in sublist]
     ingsObj = []
     for ing in ings:
          ingJ = {
               "name": ing[:50], # max_length=100
               "ingredient_id": str(uuid.uuid4())
          }
          ingsObj.append(ingJ)
          IngredientType(**ingJ).save()
     
     return ingsObj


def menu_objects():
     menu = get_menu()
     menuObj = []
     for item in menu.keys():
          itemJ = {
               "name": item[:50], # max_length=100
               "item_id": str(uuid.uuid4()),
               "price": Decimal(random.randrange(100, 1000))/100,
               "alergies": random.sample(alergies, random.randrange(1, 3))
          }
          menuObj.append(itemJ)
          MenuItem(**itemJ).save()
     return menuObj


def menu_ingredients(menu_items, ingredients):
     menuIng = []
     for item in menu_items:
          # random 2 to 5 ingredients that are unique
          ing = random.sample(ingredients, random.randrange(2, 5))
          ing = [a for a in ing if a["ingredient_id"] not in [b["ingredient_id"] for b in menuIng]]
          for i in ing:
               a = {
                    "ingredient_id": i["ingredient_id"],
                    "item_id": item["item_id"]
               }
               print(a)
               menuIng.append(a)
               MenuIngredient(**a).save()
     return menuIng



def clear_db():
     MenuItem.objects.all().delete()
     IngredientType.objects.all().delete()
     MenuIngredient.objects.all().delete()
     Order.objects.all().delete()
     Payment.objects.all().delete()
     print("DB cleared")




def main():
     clear_db()
     ings = get_ingredients()
     menus = menu_objects()
     menu_ingredients(menus, ings)
     print("DB populated")


main()