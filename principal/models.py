from django.db import models

# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=35)
    rut = models.PositiveIntegerField()
    correo = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre