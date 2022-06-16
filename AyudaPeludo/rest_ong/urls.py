from django.urls import path
from rest_ong.views import lista_pets

urlpatterns = [
    path('lista_pets', lista_pets, name="lista_pets")
]
