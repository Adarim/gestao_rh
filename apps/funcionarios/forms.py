from django.forms import ModelForm
from .models import Funcionario
from apps.departamentos.models import Departamento
from django import forms

class FuncionarioForm(ModelForm):
    nome= forms.CharField(label="Nome do Funcionário", max_length=45)
    endereco= forms.CharField(label="Endereço/Logradouro", max_length=55)
    fone= forms.CharField(label="Fone/Whats", max_length=20)
    complemento= forms.CharField(max_length=40)
    cidade= forms.CharField(max_length=35)


    def __init__(self, user, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)
        self.fields['departamentos'].queryset = Departamento.objects.filter(
            empresa=user.funcionario.empresa)

    class Meta:
        model = Funcionario
        fields = ['nome', 'departamentos', 'foto', 'endereco', 'cidade', 'complemento']
