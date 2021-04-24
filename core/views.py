from django.shortcuts import render
from django.db import connection #traera la conexion de oracle y los procesos almacenados
import cx_Oracle #libreria de oracle

# Create your views here.

def usuarios(request):
    #data sirve para pasar datos
    data = {
        'usuarios':listado_usuarios(),
        'tipousuario':listado_tipo(),
    }
    #guarda los usuarios
    if request.method == 'POST':
        nom_usuario = request.POST.get('nombre')
        clave = request.POST.get('contraseña')
        tipo_usuario = request.POST.get('tipo')
        salida = agregar_usuario(nom_usuario, clave, tipo_usuario)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['usuarios'] = listado_usuarios()
        else:
            data['mensaje'] = 'no se ha podido guardar'

    return render(request, 'core/usuarios.html', data)

# Crear metodo para el listado

def listado_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() # cursor que permite llamar al proceso directamente
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_USUARIOS",[out_cur])

    lista = []#lista para recorrer el cursor
    for fila in out_cur:
        lista.append(fila)
    
    return lista

def listado_tipo():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() # cursor que permite llamar al proceso directamente
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_TIPOUSUARIO",[out_cur])

    lista = []#lista para recorrer el cursor
    for fila in out_cur:
        lista.append(fila)
    
    return lista
#crea un nuevo usuario
def agregar_usuario(nom_usuario, clave, tipo_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() # cursor que permite llamar al proceso directamente
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_USUARIO',[nom_usuario, clave, tipo_usuario, salida])
    return salida.getvalue()

