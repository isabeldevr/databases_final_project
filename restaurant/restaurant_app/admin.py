from django.contrib import admin
from .models import MenuItem, IngredientType, MenuIngredient, Order, Payment


admin.site.register(MenuItem)
admin.site.register(IngredientType)
admin.site.register(MenuIngredient)
admin.site.register(Order)
admin.site.register(Payment)
