from django.contrib import admin
from .models import Proyectino
from .models import EstadoActividades
from .models import Programa
from .models import Tipo
from .models import Proyecto

# Register your models here.

admin.site.register(Proyectino)
admin.site.register(EstadoActividades)
admin.site.register(Programa)
admin.site.register(Tipo)
admin.site.register(Proyecto)