from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Avg
from .models import Order, Payment

def average_order_view(request):
     order = Order.objects.all()
     payment = Payment.objects.all()
     # Get average order amount
     average_order_amount = payment.aggregate(Avg('amount'))['amount__avg']

     # Pass the average order amount to the template
     return render(request, 'average_order.html', {'average_order_amount': average_order_amount})