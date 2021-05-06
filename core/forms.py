from django import forms
from django.forms import ModelForm
from .models import Usuario, Cliente, TipoUsuario, Huesped, Pedido, Factura, OrdenCompra
from django.contrib.auth.forms import UserCreationForm #registro de usuario
from django.contrib.auth.models import User


class UsuarioForm(ModelForm):


    class Meta:
        model = Usuario
        fields = ["nom_usuario","clave","tipo_usuario"]
        widgets = {
            'clave':forms.PasswordInput()
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email", "password1", "password2"]

class ClienteForm(ModelForm):


    class Meta:
        model = Cliente
        fields = '__all__'

class HuespedForm(ModelForm):
    class Meta:
        model = Huesped
        fields = '__all__'

class OrdenPedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ["cod_factura","fecha_factura","detalle_factura","valor_factura","valor_iva"]
        widgets = {
            'fecha_factura':forms.SelectDateWidget
        }


class OrdenCompraForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ["nombre_producto","cantidad","fecha_emision_pedido","fecha_recepcion"]
        widgets = {
            'fecha_emision_pedido':forms.SelectDateWidget,
            'fecha_recepcion':forms.SelectDateWidget
        }
