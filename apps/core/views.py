from django.shortcuts import render
from apps.funcionarios.models import Funcionario
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    data = {}
    data["usuario"] = request.user
    return render(request, 'core/index.html', data)