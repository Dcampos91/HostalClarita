from django import forms
from .models import Usuario

class InicioForm(forms.ModelForm): 

    class Meta:
        model = Usuario
        fields = ["nom_usuario","clave","tipo_usuario"]
