from pyexpat import model
from django.db import models

# Create your models here.
class familia(models.Model):
    familiar = models.CharField(max_length=30)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    edad = models.IntegerField()


