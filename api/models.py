from django.db import models

# Create your models here.

class Proyectino(models.Model):
    id = models.AutoField(primary_key = True)
    codigoproyecta = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    facultad = models.CharField(max_length=6)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return '{0},{1}'.format(self.nombre, self.apellido)

