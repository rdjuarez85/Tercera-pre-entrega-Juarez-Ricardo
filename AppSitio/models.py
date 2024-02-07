from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Trabajo(models.Model):
    dispositivo = models.CharField(max_length=50)
    falla = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.dispositivo}, {self.estado}"