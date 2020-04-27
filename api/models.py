from django.db import models

# Create your models here.

class Proyectino(models.Model):
    id = models.AutoField(primary_key = True)
    codigoproyecta = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    facultad = models.CharField(max_length=6)
    especialidad = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = 'proyectinos', max_length=255, blank=True, null=True)

    def __str__(self):
        return '{0},{1}'.format(self.nombre, self.apellido)

class EstadoActividades(models.Model):
    estado = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return '{0},{1}'.format(self.estado, self.descripcion)

class Programa(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_programa = models.CharField(max_length=250)
    descripcion = models.TextField(default = "")
    imagen = models.ImageField(upload_to = 'programas', max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank = True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.ForeignKey(EstadoActividades, on_delete=models.CASCADE, help_text="Indicar el estado del programa: Activo/Inactivo/Finalizado/Cancelado")

    def __str__(self):
        return '{0},{1},{2},{3}'.format(self.nombre_programa, self.descripcion, self.fecha_inicio, self.estado)

class Tipo(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return '{0},{1}'.format(self.tipo, self.descripcion)

class Proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_proyecto = models.CharField(max_length=150)
    siglas = models.CharField(max_length=15)
    descripcion = models.TextField(default = "")
    edicion = models.CharField(max_length=10)
    fecha_inicio = models.DateField(blank = True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    imagen = models.ImageField(upload_to = 'proyectos', max_length=255, blank=True, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoActividades, on_delete=models.CASCADE, help_text="Indicar el estado del programa: Activo/Inactivo/Finalizado/Cancelado")
    nombre_programa = models.ForeignKey(Programa, on_delete=models.CASCADE, blank=True ,null=True)

    def __str__(self):
        return '{0},{1},{2}'.format(self.nombre_proyecto, self.tipo, self.estado)

