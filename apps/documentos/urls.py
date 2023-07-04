from django.urls import path
from . views import  DocumentoNovo, DocumentoDelete

urlpatterns = [
     path("novo/<int:funcionario_id>/", DocumentoNovo.as_view(),  name='create-documento'),
     path("deletar/<int:pk>/", DocumentoDelete.as_view(),  name='delete-documento'),

]