from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from .forms import FuncionarioForm
from django.shortcuts import get_object_or_404, render


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioNovo(CreateView):
            model = Funcionario
            form_class = FuncionarioForm
        #    fields = ['nome','endereco','cidade','complemento','foto']

            def form_valid(self, form):
                    funcionario = form.save(commit=False)
                    funcionario.empresa = self.request.user.funcionario.empresa
                    username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
                    funcionario.user = User.objects.create(username=username)
                    funcionario.save()
                    return super(FuncionarioNovo, self).form_valid(form)

            def get_form_kwargs(self):
                    kwargs = super(FuncionarioNovo, self).get_form_kwargs()
                    kwargs.update({'user': self.request.user})
                    return kwargs


class FuncionarioEdit(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm

    def get_form_kwargs(self):
        kwargs = super(FuncionarioEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list-funcionarios')


class FuncionarioDetalhe(DetailView):
    model = Funcionario

    def funcionariodetalhe_view(request, primary_key):
        empregado = get_object_or_404(Funcionario, pk=primary_key)
        return render(request, 'funcionario_detail.html', context={'Funcionario': empregado})