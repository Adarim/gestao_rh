from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioNovo(CreateView):
     model = Funcionario
     fields = ['nome', 'departamentos', 'foto', 'endereco', 'cidade', 'complemento']

     def form_valid(self, form):
         funcionario = form.save(commit=False)
         funcionario.empresa = self.request.user.funcionario.empresa
         username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
         funcionario.user = User.objects.create(username=username)
         funcionario.save()
         return super(FuncionarioNovo, self).form_valid(form)


class FuncionarioEdit(UpdateView):
     model = Funcionario
     fields = ['nome', 'fone', 'departamentos', 'foto', 'endereco', 'cidade', 'complemento']

class FuncionarioDelete(DeleteView):
     model = Funcionario
     success_url =  reverse_lazy('list-funcionarios')
