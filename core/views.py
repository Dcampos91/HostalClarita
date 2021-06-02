from django.forms.widgets import DateTimeBaseInput
from django.shortcuts import render, redirect, get_object_or_404
from .models import TipoHabitacion, Usuario, Pedido
from .forms import UsuarioForm, CustomUserCreationForm, ClienteForm, HuespedForm, OrdenPedidoForm, HuespedForm, FacturaForm, OrdenCompraForm
from django.contrib import messages #permite enviar mensajes
from django.core.paginator import Paginator #para dividir las paginas con los usuarios agregados
from django.http import Http404, request
from django.contrib.auth import authenticate, login #autentica usuario
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection #trae la coneccion de la base de datos
import cx_Oracle


#crear vista
def home(request):#la pagina de inicio
    return render(request,'core/home.html')
@permission_required('core.view_cliente')
def listado_usuario(request):
    usuario = Usuario.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(usuario, 5)
        usuario = paginator.page(page)
    except:
        raise Http404

    data ={
        'entity':usuario,
        'paginator':paginator
    }
    return render(request, 'core/listado_usuarios.html', data)
    
@permission_required('core.add_usuario')
def nuevo_usuario(request):
    data = {
        'form':UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario Agregado Correctamente")
            

    return render(request, 'core/nuevo_usuario.html', data)

@permission_required('core.change_usuario')
def modificar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    data = {
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")#envia el mensaje
            return redirect(to="listado_usuario")
        data["form"] = formulario    
    return render(request, 'core/modificar.html', data)

@permission_required('core.delete_usuario')
def eliminar_usuario(request, id_usuario):

    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    usuario.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listado_usuario")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Cliente registrado correctamente")
            return redirect(to='/')
        data["form"] = formulario 

    return render(request,'registration/registro.html', data)

@permission_required('core.add_cliente')
def nueva_empresa(request):
    data = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Empresa registrada")
            return redirect(to='home')
    return render(request, 'core/empresa.html', data)

@permission_required('core.add_cliente')
def huesped_registro(request):
    data = {
        'form': HuespedForm()
    }
    if request.method == 'POST':
        formulario = HuespedForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Huesped registrado")
            return redirect(to='home')  
        data["form"] = formulario     
    return render(request, 'core/huesped.html', data)

@permission_required('core.add_cliente')
def recepcion_pedido(request):
    return render(request, 'core/recepcion_pedido.html')

@permission_required('core.view_pedido')
def orden_pedido(request):
    pedido = Pedido.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(pedido, 5)
        pedido = paginator.page(page)
    except:
        raise Http404

    data ={
        'entity':pedido,
        'paginator':paginator
    }

    return render(request, 'core/recepcion_pedido.html', data)

@permission_required('core.view_pedido')
def recepcion_pedido(request):
    pedido = Pedido.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(pedido, 5)
        pedido = paginator.page(page)
    except:
        raise Http404

    data ={
        'entity':pedido,
        'paginator':paginator
    }
    return render(request, 'core/recepcion_pedido.html', data)

@permission_required('core.add_cliente')
def orden_compra(request):
    data = {
        'form': OrdenCompraForm()
    }
    if request.method == 'POST':
        formulario = OrdenCompraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Orden registrada")
            return redirect(to='home')  
        data["form"] = formulario     
    return render(request, 'core/orden_compra.html', data)

@permission_required('core.add_cliente')
def registro_factura(request):
    data = {
        'form': FacturaForm()
    }
    if request.method == 'POST':
        formulario = FacturaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Factura registrada")
            return redirect(to='home')  
        data["form"] = formulario     
    return render(request, 'core/factura.html', data)

def registro_habitacion(request):
    tiphab = TipoHabitacion.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tiphab, 6)
        tiphab = paginator.page(page)
    except:
        raise Http404

    data ={
        'entity':tiphab,
        'paginator':paginator
    }
    
    return render(request,'core/registro_habitacion.html',data)

def registro_proveedor(request):
    data = {
        'registro_proveedor':listar_proveedor()
    }

    if request.method == 'POST':
        rut_proveedor = request.POST.get('rut') 
        nom_proveedor = request.POST.get('nombre') 
        rubro_proveedor = request.POST.get('rubro') 
        tel_proveedor = request.POST.get('telefono') 
        salida = agregar_proveedor(rut_proveedor,nom_proveedor,rubro_proveedor,tel_proveedor)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['registro_proveedor'] = listar_proveedor()
        else:
            data['mensaje'] = 'no se ha guardado'

    return render(request, 'core/registro_proveedor.html',data)

def listar_proveedor():   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROVEEDOR", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def agregar_proveedor(rut_proveedor, nom_proveedor, rubro_proveedor, tel_proveedor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PROVEEDOR',[rut_proveedor,nom_proveedor,rubro_proveedor,tel_proveedor,salida])     
    return salida.getvalue()


def reserva_huesped(request):
    data = {
        'empresa':listado_empresa(),
        'huesped':listado_huesped(),
        'habitacion':listado_habitacion(),
        'listado_huesped':listado_huespedes()
    }
    if request.method == 'POST':
        rut_empresa = request.POST.get('rut empresa') 
        rut_huesped = request.POST.get('rut huesped') 
        id_tipo_habitacion = request.POST.get('id tipo habitacion') 
        check_in = request.POST.get('check_in') 
        check_out = request.POST.get('check_out')
        salida = registrar_reserva(rut_empresa,rut_huesped,id_tipo_habitacion,check_in,check_out)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['listado_huesped'] = listado_huespedes()
        else:
            data['mensaje'] = 'no se ha guardado'
    return render(request, 'core/reserva_huesped.html',data)  

def listado_empresa():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RUTEMPRESA", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_huesped():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RUTHUESPED", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_habitacion():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_IDHABITACION", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_huespedes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RESERVA", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def registrar_reserva(rut_empresa,rut_huesped,id_tipo_habitacion,check_in,check_out):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_GENERAR_RESERVA',[rut_empresa,rut_huesped,id_tipo_habitacion,check_in,check_out,salida])     
    return salida.getvalue()

def menu_admin(request):
    return render(request,'core/menuadmin.html')

def comedor(request):
    data = {
        'comedor':listar_comedor()
    }
    if request.method == 'POST':
        nombre_plato = request.POST.get('nombre') 
        detalle = request.POST.get('detalle') 
        valor_plato = request.POST.get('valor') 
        tipo_servicio = request.POST.get('servicio') 
        salida = registrar_comedor(nombre_plato,detalle,valor_plato,tipo_servicio)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['comedor'] = listar_comedor()
        else:
            data['mensaje'] = 'no se ha guardado'

    return render(request,'core/comedor.html',data)

def listar_comedor():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_COMEDOR", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def registrar_comedor(nombre_plato,detalle,valor_plato,tipo_servicio):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_COMEDOR',[nombre_plato,detalle,valor_plato,tipo_servicio,salida])     
    return salida.getvalue()



