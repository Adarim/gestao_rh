from django.forms import ModelForm
from .models import Departamento
from django import forms

class DepartamentoForm(ModelForm):
    nome= forms.CharField(label="Nome do Departamento", max_length=45)
    encarregado= forms.CharField(label="Nome do Encarregado", max_length=45, required=False)
    localizacao= forms.CharField(label="Localização do Depto.", max_length=50, required=False)


    class Meta:
        model = Departamento
        fields = ['nome', 'encarregado', 'localizacao']
