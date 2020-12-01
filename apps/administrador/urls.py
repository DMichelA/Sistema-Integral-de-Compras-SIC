from django.urls import path, include

from apps.administrador.views import index, verificacion_bienes, bienes_adjudicar

urlpatterns = [
    path('', index, name="administrador_index"),
    path('verificacion_bienes/', verificacion_bienes, name="verificacion_bienes"),
    path('bienes_adjudicar/<int:id_bien>/', bienes_adjudicar, name="adjudicion_bienes"),
]