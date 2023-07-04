from django.urls import path
from . views import  DepartamentosList, \
    DepartamentoNovo, \
    DepartamentoEdit,\
    DepartamentoDelete
1
urlpatterns = [
    path("list", DepartamentosList.as_view(),  name='list-departamentos'),
    path("novo/", DepartamentoNovo.as_view(),  name='create-departamento'),
    path("editar/<int:pk>/", DepartamentoEdit.as_view(),  name='edit-departamento'),
    path("deletar/<int:pk>/", DepartamentoDelete.as_view(),  name='delete-departamento'),
]