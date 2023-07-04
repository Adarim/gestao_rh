from django.urls import path
from django.conf.urls.static import static

from gestao_rh import settings
from . views import  FuncionariosList, \
    FuncionarioNovo, \
    FuncionarioEdit,\
    FuncionarioDelete

urlpatterns = [
    path("", FuncionariosList.as_view(),  name='list-funcionarios'),
    path("novo/", FuncionarioNovo.as_view(),  name='create-funcionario'),
    path("editar/<int:pk>/", FuncionarioEdit.as_view(),  name='edit-funcionario'),
    path("deletar/<int:pk>/", FuncionarioDelete.as_view(),  name='delete-funcionario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)