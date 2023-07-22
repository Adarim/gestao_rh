from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=60)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    post = models.DateTimeField(auto_now_add=True)
    utilizada = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detalhe-funcionario', args=[self.funcionario.id])

    def __str__(self):
        return self.motivo