from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.models import Pet
from .serializers import PetSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        pet_serializer = PetSerializer(pets, many=True)
        return Response(pet_serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        pet_serializer = PetSerializer(data=data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            return Response(pet_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

