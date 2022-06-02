from django.shortcuts import render
from .models import Pet

def home(request):
    pets = Pet.objects.all()
    
    datos = {
        'pets': pets
    }
    return render(request, 'core/home.html', datos)
