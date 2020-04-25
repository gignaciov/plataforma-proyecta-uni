from django.urls import path
from .views import ProyectinoListCreate,ProyectoListCreate
from .views import UserList
from .views import HelloView

urlpatterns = [
    # url(r'^$', views.index, name='index'),        Esta es una manera antigua de hacerlo
    path('users/', UserList.as_view(), name = 'user_list'),
    path('proyectinos/', ProyectinoListCreate.as_view(), name = 'proyectino_list'),
    path('proyectos/', ProyectoListCreate.as_view(), name = 'proyecto_list'),
    path('hello/', HelloView.as_view(), name='hello'),
    
]
