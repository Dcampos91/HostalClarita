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
    path('huesped', huesped_registro, name="huesped"),
    path('recepcion-pedido', recepcion_pedido, name="recepcion_pedido"),
    path('orden-compra', orden_compra, name="orden_compra"),
    path('orden-pedido', orden_pedido, name="orden_pedido"),
    path('factura-registro', registro_factura, name="factura"),
    path('registro-habitacion', registro_habitacion, name="registro_habitacion"),
    path('registro-proveedor', registro_proveedor, name="registro_proveedor"),
    path('reserva-huesped', reserva_huesped, name="reserva_huesped"),
    path('menu-admin', menu_admin, name="menu_admin"),
    path('comedor', comedor , name="comedor"),
    #prueba1
    
  
    
    
]