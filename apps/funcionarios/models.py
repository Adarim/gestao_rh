from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.urls import reverse
from django.db.models import Sum


class Funcionario(models.Model):
    nome = models.CharField(max_length=60, verbose_name = "Nome do Funcionário")
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento, verbose_name = "Departamentos Participantes")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    foto = models.FileField(upload_to='documentos', null=True, blank=True)
    fone = models.CharField(max_length=30, verbose_name = "Contato(Whats)")
    endereco = models.CharField(max_length=50, null=True, blank=True, verbose_name = "Endereço")
    cidade = models.CharField(max_length=35, null=True, blank=True)
    complemento = models.CharField(max_length=35, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list-funcionarios')

    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.filter(utilizada=False).aggregate(Sum('horas'))['horas__sum']
        return total or 0

    @property
    def total_horas_util(self):
        total = self.registrohoraextra_set.filter(utilizada=True).aggregate(Sum('horas'))['horas__sum']
        return total or 0
