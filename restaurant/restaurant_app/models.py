from django.db import models
# import option to have list 
import uuid

def generate_uuid():
    return str(uuid.uuid4())


class MenuItem(models.Model):
     item_id = models.CharField(primary_key=True, max_length=100, default=generate_uuid(), editable=False)
     name = models.CharField(max_length=100)
     price = models.DecimalField(max_digits=6, decimal_places=2)
     # alergies is a list of strings
     alergies = models.JSONField()
     
     class Meta:
          app_label = 'restaurant_app'
     
class IngredientType(models.Model):
     name = models.CharField(max_length=100)
     ingredient_id = models.CharField(primary_key=True, max_length=100, default=generate_uuid(), editable=False)
     

     

class MenuIngredient(models.Model):
     ingredient_id = models.CharField(primary_key=True, max_length=100, default=generate_uuid(), editable=False)
     item_id = models.CharField(max_length=100, default=generate_uuid(), editable=False)



class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=100, default=generate_uuid(), editable=False)
    item = models.CharField(max_length=100, default=generate_uuid(), editable=False)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.order_id}"

class Payment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=100, default=generate_uuid(), editable=False)
    order = models.CharField(max_length=100, default=generate_uuid(), editable=False)
    method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.payment_id}"