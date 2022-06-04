from django.db import models

class Pet(models.Model):
    idPet = models.IntegerField(primary_key=True, verbose_name="Id de mascota")
    name = models.CharField(max_length=200, verbose_name="Nombre mascota")
    
    def __str__(self):
        return self.name
