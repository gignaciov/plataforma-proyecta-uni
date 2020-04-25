# Este archivo nos ayuda a convertir data a un tipo de archivo de intercambio
# de información entre aplicaciones, lenguajes o proyectos. (tipo de formatos 
# más comun es XML o JSON)
from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Proyectino
from .models import Proyecto

class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        # Specify the model we are using
        model = User
        # Specify the fields that should be made accessible.
        # Mostly it is all fields in that model
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')

class ProyectinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectino
        fields = (
            'id',
            'codigoproyecta',
            'nombre',
            'apellido',
            'facultad',
            'especialidad',
        )

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = (
            'id',
            'nombre_proyecto',
            'siglas',
            'descripcion',
            'edicion',
            'fecha_inicio',
            'fecha_fin',
            'imagen',
            'tipo',
            'estado',
            'nombre_programa',
        )