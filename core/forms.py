from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class InicioForm(forms.ModelForm):


    class Meta:
        model = Usuario
        fields = ["nom_usuario","clave","tipo_usuario"]




