from django.shortcuts import render
from order.models import Coffee


def order(request):
    coffees = Coffee.objects.all()
    return render(request, 'order/order.html', {'coffees': coffees})

