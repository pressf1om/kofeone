from django.shortcuts import render

def recept(request):
    return render(request, 'recept/recept.html')
