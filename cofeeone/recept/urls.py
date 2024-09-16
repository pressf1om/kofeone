from django.contrib import admin
from django.urls import path, include
from recept.views import recept

urlpatterns = [
    path('', recept, name='recept'),
]