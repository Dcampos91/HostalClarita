from django import forms
from django.forms import ModelForm
from .models import Usuario


class UsuarioForm(ModelForm):


    class Meta:
        model = Usuario
        fields = ["id_usuario","nom_usuario","clave","tipo_usuario"]




