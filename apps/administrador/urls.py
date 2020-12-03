from django.urls import path, include

from apps.administrador.views import index, listado_bienes, bienes_adjudicar, bienes_adjudicados, \
actualizar_bienes, eliminar_bienes

urlpatterns = [
    path('', index, name="administrador_index"),
    path('listado_bienes/', listado_bienes, name="listado_bienes"),
    path('bienes_adjudicar/<int:id_bien>/', bienes_adjudicar, name="adjudicion_bienes"),
    path('bienes_adjudicados/', bienes_adjudicados, name="bienes_adjudicados"),
    path('actualizar_bienes/<int:id_bien>/', actualizar_bienes, name="actualizar_bienes"),
    path('eliminar_bienes/<int:id_bien>/', eliminar_bienes, name="eliminar_bienes"),
]
