from django.urls import path
from . views import HoraExtraList,  \
    HoraExtraNovo,   \
    HoraExtraEdit,  \
    HoraExtraDelete

urlpatterns = [
    path("", HoraExtraList.as_view(),  name='list-hora-extra'),
    path("novo/", HoraExtraNovo.as_view(),  name='create-hora-extra'),
    path("editar/<int:pk>/", HoraExtraEdit.as_view(),  name='edit-hora-extra'),
    path("deletar/<int:pk>/", HoraExtraDelete.as_view(),  name='delete-hora-extra'),
]