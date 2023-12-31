from django.db import models
from django.urls import reverse
from apps.empresas.models import  Empresa


class Departamento(models.Model):
    nome = models.CharField(max_length=70, help_text='Nome do Departamento')
    empresa =  models.ForeignKey(Empresa, on_delete=models.PROTECT)
    encarregado = models.CharField(max_length=50, help_text='Encarregado', null=True, blank=True)
    localizacao = models.CharField(max_length=100, help_text="Localização", null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list-departamentos')