from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Pet

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields  = ['name']
