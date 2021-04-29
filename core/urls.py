from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home, name="home"),
    path('usuario', usuarios, name='usuarios'),
    path('empleado', empleado, name='empleado'),
    path('proveedor', proveedor, name='proveedor'),
    path('eliminar', eliminar_usuario, name='eliminar'),
    
    
]