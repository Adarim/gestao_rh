from django.http import request

from .forms import DepartamentoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, \
    UpdateView, DeleteView, CreateView, View
from .models import Departamento


class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoNovo(CreateView):
     model = Departamento
     form_class = DepartamentoForm

     def form_valid(self, form):
         departamento = form.save(commit=False)
         departamento.empresa = self.request.user.funcionario.empresa
         departamento.save()
         return super(DepartamentoNovo, self).form_valid(form)


class DepartamentoEdit(UpdateView):
     model = Departamento
     form_class = DepartamentoForm


class DepartamentoDelete(DeleteView):
     model = Departamento
     success_url =  reverse_lazy('list-departamentos')


class Exclui_depto(View):
    def delete(request, pk):
        db = Departamento.objects.get(pk=pk)
        db.delete()
        return HttpResponseRedirect(reverse('home'))