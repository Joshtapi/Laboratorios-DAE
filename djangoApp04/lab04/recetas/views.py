from django.shortcuts import render
from .models import Receta

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista_recetas.html', {'recetas': recetas})

def index(request):
    return render(request, 'index.html')