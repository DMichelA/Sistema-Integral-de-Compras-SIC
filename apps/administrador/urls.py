from django.urls import path, include

from apps.administrador.views import index, verificacion_bienes

urlpatterns = [
    path('', index, name="administrador_index"),
    path('verificacion_bienes/', verificacion_bienes, name="verificacion_bienes"),
]