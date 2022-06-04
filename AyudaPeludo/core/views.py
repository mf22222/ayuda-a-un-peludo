from django.shortcuts import render
from .models import Pet
from .forms import PetForm

def home(request):
    pets = Pet.objects.all()
    
    datos = {
        'pets': pets
    }
    return render(request, 'core/home.html', datos)

def form_pets(request):
    datos = {
        'form': PetForm()
    }
    
    if request.method == 'POST':
        formulario = PetForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['message'] = 'Guardado correctamente'
        else:
            datos['message'] = 'Hubo un problema'
    
    
    return render(request, 'core/form_pets.html', datos)
