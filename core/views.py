from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm, CustomUserCreationForm, ClienteForm
from django.contrib import messages #permite enviar mensajes
from django.core.paginator import Paginator #para dividir las paginas con los usuarios agregados
from django.http import Http404
from django.contrib.auth import authenticate, login #autentica usuario

#crear vista
def home(request):#la pagina de inicio
    return render(request,'core/home.html')

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

def eliminar_usuario(request, id_usuario):

    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    usuario.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listado_usuario")

def registro(request):
    data = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(nom_usuario=formulario.cleaned_data["nom_usuario"], clave=formulario.cleaned_data["clave"])
            #login(request, user)
            messages.success(request, "Cliente registrado correctamente")
            return redirect(to='empresa')
        data["form"] = formulario 

    return render(request,'registration/registro.html', data)

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


    