from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.models import Pet
from .serializers import PetSerializer

@csrf_exempt
@api_view(['GET'])
def lista_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        pet_serializer = PetSerializer(pets, many=True)
        return Response(pet_serializer.data)

