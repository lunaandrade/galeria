from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'galeria/home.html')

def galeria(request):
    return render(request, 'galeria/galeria.html')

def sobre(request):
    return render(request, 'galeria/sobre.html')
