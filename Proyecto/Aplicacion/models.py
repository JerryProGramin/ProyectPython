from django.db import models

# Create your models here.

class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=40)
    edad=models.IntegerField()
    telefono=models.CharField(max_length=9)

    def __str__(self) -> str:
        return self.nombre

class Mascota(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    persona=models.ForeignKey(Persona,on_delete=models.CASCADE, editable=True)

    def __str__(self) -> str:
        return self.nombre