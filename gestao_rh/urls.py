from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from gestao_rh import settings


urlpatterns = [
    path('', include('apps.core.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
