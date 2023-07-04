from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import Documento


class DocumentoNovo(CreateView):
     model = Documento
     fields = ['descricao', 'arquivo']

     def post(self, request, *args, **kwargs):
          form = self.get_form()
          form.instance.pertence_id = self.kwargs['funcionario_id']
          if form.is_valid():
               return self.form_valid(form)
          else:
               return self.form_invalid(form)

class DocumentoDelete(DeleteView):
          model = Documento
          success_url =  reverse_lazy('list-funcionarios')