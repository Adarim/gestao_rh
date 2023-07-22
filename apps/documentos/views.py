from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import Documento
from .forms import DocumentoForm, DocFunForm


class DocumentoNovo(CreateView):
     model = Documento
     form_class = DocumentoForm

     def post(self, request, *args, **kwargs):
          form = self.get_form()
          form.instance.pertence_id = self.kwargs['funcionario_id']
          if form.is_valid():
               return self.form_valid(form)
          else:
               return self.form_invalid(form)

     def get_form_kwargs(self):
         kwargs = super(DocumentoNovo, self).get_form_kwargs()
         kwargs.update({'user': self.request.user})
         return kwargs


class DocFunNovo(CreateView):
     model = Documento
     form_class = DocFunForm

     def post(self, request, *args, **kwargs):
          form = self.get_form()
          form.instance.pertence_id = self.kwargs['funcionario_id']
          if form.is_valid():
               return self.form_valid(form)
          else:
               return self.form_invalid(form)


class DocumentoDelete(DeleteView):
     model = Documento

     def get_success_url(self):
         return reverse_lazy('detalhe-funcionario', args=[self.kwargs['funcionario_id']])