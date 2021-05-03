from django import forms
from django.forms import ModelForm
from .models import Usuario, Cliente
from django.contrib.auth.forms import UserCreationForm #registro de usuario
from django.contrib.auth.models import User


class UsuarioForm(ModelForm):


    class Meta:
        model = Usuario
        fields = ["id_usuario","nom_usuario","clave","tipo_usuario"]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email", "password1", "password2"]

class ClienteForm(ModelForm):


    class Meta:
        model = Cliente
        fields = '__all__'
