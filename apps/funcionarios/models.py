from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.urls import reverse

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT, help_text='Usuário')
    departamentos = models.ManyToManyField(Departamento,)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)
    foto = models.FileField(upload_to='documentos', null=True, blank=True)
    fone = models.CharField(max_length=30,help_text='Fone/Whatsapp')
    endereco = models.CharField(max_length=50,help_text='Endereço', null=True, blank=True)
    cidade = models.CharField(max_length=35, null=True, blank=True)
    complemento = models.CharField(max_length=35, null=True, blank=True)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list-funcionarios')