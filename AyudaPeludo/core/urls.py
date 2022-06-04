from django.urls import path
from .views import home, form_pets

urlpatterns = [
    path('', home, name="home"),
    path('form-pets', form_pets, name="form_pets")
]


