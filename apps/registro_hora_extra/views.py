import json

from django.core.paginator import Paginator
from django.http import HttpResponse,  JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm, RegFunHEForm, LoteHEForm
from ..funcionarios.models import Funcionario
from django.db.models import Sum, Count


class HoraExtraList(ListView):
    model = RegistroHoraExtra
    context_object_name = 'Registro Hora-Extra'
    paginate_by = 8

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        txt_motivo = self.request.GET.get('pmotivo')
        if txt_motivo:
            he = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada, motivo__icontains=txt_motivo)
        else:
            he = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return he


class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list-hora-extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HEFunNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegFunHEForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list-hora-extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEditFunc(UpdateView):
    model = RegistroHoraExtra
    form_class = RegFunHEForm

    def get_success_url(self):
        return reverse_lazy('detalhe-funcionario', args=[self.kwargs['funcionario_id']])


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list-hora-extra')


class HEFunDelete(DeleteView):
    model = RegistroHoraExtra

    def get_success_url(self):
        return reverse_lazy('detalhe-funcionario', args=[self.kwargs['funcionario_id']])


class utilHE(View):

    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()
        funcionario=self.request.user.funcionario
        response = json.dumps({'mensagem': 'Hora-Extra marcada como utilizada com sucesso',
                                                 'horas': float(funcionario.total_horas_extra)})
        return HttpResponse(response, content_type='application/json')


class Nao_utilHE(View):

    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada =False
        registro_hora_extra.save()
        funcionario=self.request.user.funcionario
        response = json.dumps({'mensagem': 'Utilização da hora-Extra desmarcada com sucesso',
                                                  'horas': float(funcionario.total_horas_extra)})
        return HttpResponse(response, content_type='application/json')


def delete(request, pk):
    db = RegistroHoraExtra.objects.get(pk=pk)
    db.delete()
    return redirect('list-hora-extra')


def marca(request, pk):
    db = RegistroHoraExtra.objects.get(pk=pk)
    db.utilizada=True
    db.save()
    return redirect('list-hora-extra')


def desmarca(request, pk):
    db = RegistroHoraExtra.objects.get(pk=pk)
    db.utilizada=False
    db.save()
    return redirect('list-hora-extra')


def HoraExtraLote(request, *args, **kwargs):
    txt_motivo = request.GET.get('pmotivo')
    txt_status = request.GET.get('status')
    txt_func = request.GET.get('pfunc')
    txt_ad = request.GET.get('vad')
    txt_pq = request.GET.get('vpq')
    if txt_ad != False: txt_ad = True
    if txt_pq != False: txt_pq = True

    he = RegistroHoraExtra.objects.filter(funcionario__empresa=kwargs['pk'])
    if txt_motivo:
       he=he.filter(motivo__icontains=txt_motivo)
    if txt_func:
       he=he.filter(funcionario__id=txt_func)
    if txt_status != 'Todas':
        if txt_status == 'Usadas':
            he = he.filter(utilizada=True)
        else:
            he = he.filter(utilizada=False)

    tot_lib = he.filter(utilizada=False).aggregate(Sum('horas'))['horas__sum']
    tot_util = he.filter(utilizada=True).aggregate(Sum('horas'))['horas__sum']
    tot_enc= he.count()

    funcionario_list = Funcionario.objects.filter(empresa_id=kwargs['pk'])
    if request.method == "POST":
        form = LoteHEForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-hora-ajax', kwargs['pk'])

    paginator = Paginator(he, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    form = LoteHEForm() # Formulário
    context = {"form" : form, 'funcionario_list': funcionario_list, 'tl' : tot_lib, 'tu' : tot_util, 'te' : tot_enc,  "page_obj": page_obj}
    return render(request, 'registro_hora_extra/registrohoraextra_ajax.html',  context)


def update_motivo(request):
    data_id  = request.GET.get('data_id') # Id da Lista
    motivo = request.GET.get('motivo') # Id do status
    print(data_id, motivo)

    HE = get_object_or_404(RegistroHoraExtra,id=data_id) # Get Objeto lista
    HE.motivo = motivo # status recebe novo valor "Id do status"
    HE.save() # salva

    data = {'status':'update-motivo', 'motivo':motivo}
    return JsonResponse(data) # retorna


def update_horas(request):
    data_id  = request.GET.get('data_id') # Id da Lista
    horas = request.GET.get('horas') # Id do status
    print(data_id, horas)

    HE = get_object_or_404(RegistroHoraExtra,id=data_id) # Get Objeto lista
    HE.horas = horas # status recebe novo valor "Id do status"
    HE.save() # salva

    data = {'status':'update-horas', 'horas':horas}
    return JsonResponse(data) # retorna


def update_funcionario(request):
    data_id  = request.GET.get('data_id') # Id da Lista
    funcionario_id = request.GET.get('funcionario_id') # Id do funcionario

    funcionario = Funcionario.objects.get(id=funcionario_id) # Get objeto funcionario

    HE = get_object_or_404(RegistroHoraExtra,id=data_id) # Get Objeto lista
    HE.funcionario = funcionario # funcionario recebe novo valor "Id do funcionario"
    HE.save() # salva

    data = {'funcionario':funcionario_id}
    return JsonResponse(data)



