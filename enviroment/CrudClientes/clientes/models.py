from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=65)
    apellido = models.CharField(max_length=65)
    pais = models.CharField(max_length=65)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=65)
    dni = models.CharField(
        max_length=25,
        unique=True,
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.apellido
