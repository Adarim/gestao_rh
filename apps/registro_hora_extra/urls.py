from django.urls import path

from . import views
from .views import HoraExtraList, \
    HoraExtraNovo, \
    HoraExtraEdit, \
    HoraExtraDelete, \
    HoraExtraEditFunc, \
    HEFunNovo, \
    HEFunDelete, \
    utilHE, \
    Nao_utilHE, \
    delete, desmarca, marca

urlpatterns = [
    path("", HoraExtraList.as_view(),  name='list-hora-extra'),
    path("lote/<int:pk>", views.HoraExtraLote,  name='list-hora-ajax'),
    path("novo/", HoraExtraNovo.as_view(),  name='create-hora-extra'),
    path("novofun/<int:funcionario_id>/", HEFunNovo.as_view(),  name='create-fun-hora-extra'),
    path("editar/<int:pk>/", HoraExtraEdit.as_view(),  name='edit-hora-extra'),
    path("editar-func/<int:pk>/<int:funcionario_id>", HoraExtraEditFunc.as_view(),  name='edit-hora-extra-func'),
    path("deletar/<int:pk>/", HoraExtraDelete.as_view(),  name='delete-hora-extra'),
    path("deletar-func/<int:pk>/<int:funcionario_id>", HEFunDelete.as_view(),  name='delete-fun-hora-extra'),
    path("utilizouHE/<int:pk>/", utilHE.as_view(), name='utilizou-HE'),
    path("naoutilizouHE/<int:pk>/", Nao_utilHE.as_view(), name='naoutilizou-HE'),
    path("delete/<int:pk>/", delete, name='delete'),
    path("marca/<int:pk>/", marca, name='marca'),
    path("desmarca/<int:pk>/", desmarca, name='desmarca'),
    path('update-motivo', views.update_motivo, name="update-motivo"),
    path('update-horas', views.update_horas, name="update-horas"),
    path('update-funcionario', views.update_funcionario, name="update-funcionario"),
]