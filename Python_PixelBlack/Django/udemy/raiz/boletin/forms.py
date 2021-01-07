from django import forms
from .models import Registrado


class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.IntegerField()