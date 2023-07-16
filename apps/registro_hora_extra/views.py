from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


class HoraExtraList(ListView):
   model = RegistroHoraExtra

   def get_queryset(self):
      empresa_logada = self.request.user.funcionario.empresa
      return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEdit( UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list-hora-extra')

 #   def get_success_url(self):
  #      return reverse_lazy('list-hora-extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class HoraExtraEditFunc(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

#    def get_success_url(self):
 #       return reverse_lazy('detalhe-funcionario', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditFunc, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list-hora-extra')
