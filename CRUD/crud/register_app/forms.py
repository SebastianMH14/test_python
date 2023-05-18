from django import forms
from django.forms import DateInput
from .models import Registro

class RegistroForm(forms.ModelForm):
    fecha = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Registro
        fields = ('documento', 'telefono', 'celular', 'texto1', 'texto2', 'fecha')
