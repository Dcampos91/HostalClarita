from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Pedido
from .forms import UsuarioForm, CustomUserCreationForm, ClienteForm, HuespedForm, OrdenPedidoForm, HuespedForm, FacturaForm, OrdenCompraForm
from django.contrib import messages #permite enviar mensajes
from django.core.paginator import Paginator #para dividir las paginas con los usuarios agregados
from django.http import Http404
from django.contrib.auth import authenticate, login #autentica usuario
from django.contrib.auth.decorators import login_required, permission_required
#prueba de descarga

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

    