from django.urls import path
from .views import average_order_view

urlpatterns = [
    path('average_order/', average_order_view, name='average_order'),
]