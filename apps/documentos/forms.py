from django.forms import ModelForm
from .models import Documento
from apps.funcionarios.models import Funcionario
from django import forms


class DocumentoForm(ModelForm):
    descricao= forms.CharField(label="Descrição do Documento", max_length=50)
    arquivo= forms.FileField(label="Diretório/Nome do Arquivo")

    def __init__(self, user, *args, **kwargs):
        super(DocumentoForm, self).__init__(*args, **kwargs)
        self.fields['pertence'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa)

    class Meta:
        model = Documento
        fields = ['descricao', 'arquivo', 'pertence']


class DocFunForm(ModelForm):
    descricao= forms.CharField(label="Descrição do Documento", max_length=50)
    arquivo= forms.FileField(label="Diretório/Nome do Arquivo")

    class Meta:
        model = Documento
        fields = ['descricao', 'arquivo']