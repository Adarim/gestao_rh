from django.forms import ModelForm
from .models import RegistroHoraExtra, Funcionario
from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH


class RegistroHoraExtraForm(ModelForm):
    motivo = forms.CharField(label="Descrição do Motivo da Hora-Extra", max_length=50)
    horas = forms.DecimalField(label="Quantidade de Horas", max_digits=5, decimal_places=2)

    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']
        labels = {'funcionario': 'Escolha o Funcionário'}


class RegFunHEForm(ModelForm):
    motivo = forms.CharField(label="Descrição do Motivo da Hora-Extra", max_length=50)
    horas = forms.DecimalField(label="Quantidade de Horas", max_digits=5, decimal_places=2)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo',  'horas']


class LoteHEForm(forms.ModelForm):
    motivo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Descrição(Motivo)...'}))
    horas = forms.DecimalField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Horas'}))

    class Meta:
        model = RegistroHoraExtra
        fields = ('motivo',  'horas', 'funcionario',)
        exclude = ('utilizada',)

    def __init__(self, *args, **kwargs): # Adiciona
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
              field.widget.attrs['class'] = 'form-control'


class LoteHEPesqForm(forms.ModelForm):
    motivo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Descrição(Motivo)...'}))


    class Meta:
        model = RegistroHoraExtra
        fields = ('motivo', 'funcionario',)
        exclude = ('utilizada',)

    def __init__(self, *args, **kwargs): # Adiciona
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
              field.widget.attrs['class'] = 'form-control'
