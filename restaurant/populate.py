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
import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')
django.setup()
from restaurant_app.models import MenuItem, IngredientType, MenuIngredient, Order, Payment


alergies = {'Shellfish', 'Peanut', 'Dairy', 'Wheat', 'Fish', 'Egg', 'Soy', 'Sesame', 'Gluten', 'Tree Nut'}

fake = Faker()


def get_menu():
     """Get menu items from json file. Saves to DB.
     Returns:
          [list]: [list of menu items]"""
     try:
          with open('../menu_items.json') as json_file:
               data = json.load(json_file)
               return data
     except Exception as e:
          print("Error getting menu items. Make sure that the file exists and is in the correct location.")
          print(e)
          traceback.print_exc()
          return []

def get_ingredients():
     """Get ingredients from previously saved json file from API call. Saves to DB.
     Returns:
          [list]: [list of ingredients]"""
     try: 
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
     except Exception as e:
          print("Error getting ingredients. 'Returning empty list.'Make sure that the key is working before continuing.")
          print(e)
          traceback.print_exc()
          return []


def menu_objects():
     """Creates menu objects using json file and menu. Saves to DB.
     Returns:
          [list]: [list of menu objects]"""
     try: 
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
     except Exception as e:
          print("Error getting menu items. Make sure that the file exists and is in the correct location.")
          print(e)
          traceback.print_exc()
          return []

def menu_ingredients(menu_items, ingredients):
     """Creates menu ingredients objects using json file and menu. Saves to DB.
     Returns:
          [list]: [list of menu ingredients objects]"""
     try: 
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
     except Exception as e:
          print("Error getting ingredients and menu item relationship. 'Returning empty list.'Make sure that the key is working before continuing")
          print(e)
          traceback.print_exc()
          return []


def get_orders():
     """Creates orders based on random meny items and quantities. Saves to DB
     Returns:
          [list]: [list of orders]
     """
     try: 
          orders = []
          for i in range(0, 50):
               order = {
                    "order_id": str(uuid.uuid4()),
                    "item": random.choice(MenuItem.objects.all()).item_id,
                    "quantity": random.randrange(1, 5),
                    "status": random.choice(["Pending", "Preparing", "Ready"])
               }
               orders.append(order)
               Order(**order).save()
          return orders
     except Exception as e:
          print(e)
          traceback.print_exc()
          return []

def get_payments():
     """Creates payments based on random orders and methods. Saves to DB
     Returns:
          [list]: [list of payments]
     """
     try:
          payments = []
          orders = [a.order_id for a in Order.objects.all()]
          for order in orders:
               payment = {
                         "payment_id": str(uuid.uuid4()),
                         "order": order,
                         "method": random.choice(["Cash", "Card"]),
                         "amount": Decimal(random.randrange(100, 1000))/100,
                         "status": random.choice(["Pending", "Paid"])
               }
               payments.append(payment)
               Payment(**payment).save()
          return payments
     except Exception as e:
          print(e)
          traceback.print_exc()
          return []


def clear_db():
     """Clears DB of previous data"""
     try: 
          MenuItem.objects.all().delete()
          IngredientType.objects.all().delete()
          MenuIngredient.objects.all().delete()
          Order.objects.all().delete()
          Payment.objects.all().delete()
          print("DB cleared")
     except Exception as e:
          print(e)
          traceback.print_exc()
          


def main():
     clear_db()
     ings = get_ingredients()
     menus = menu_objects()
     menu_ingredients(menus, ings)
     get_orders()
     get_payments()
     print("DB populated")
main()