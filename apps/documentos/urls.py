from django.urls import path
from django.conf.urls.static import static
from gestao_rh import settings
from . views import  DocumentoNovo, DocFunNovo, DocumentoDelete

urlpatterns = [
     path('novo/<int:funcionario_id>/', DocumentoNovo.as_view(),  name='create-documento'),
     path('novofun/<int:funcionario_id>/', DocFunNovo.as_view(),  name='create-fun-documento'),
     path('deletar/<int:pk>/ <int:funcionario_id>/', DocumentoDelete.as_view(),  name='delete-documento'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)