from django.contrib import admin
from django.urls import path, include
from order.views import order

urlpatterns = [
    path('', order, name='order'),
]