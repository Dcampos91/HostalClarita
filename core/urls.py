from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('listado-usuario', listado_usuario, name="listado_usuario"),
    path('nuevo-usuario', nuevo_usuario, name="nuevo_usuario"),
    path('modificar/<id_usuario>/', modificar_usuario, name="modificar_usuario"),
    path('eliminar/<id_usuario>/', eliminar_usuario, name="eliminar_usuario"),
    path('registro', registro, name="registro"),
    path('empresa', nueva_empresa, name="empresa"),
  
    
    
]