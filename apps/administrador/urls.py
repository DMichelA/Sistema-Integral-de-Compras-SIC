from django.urls import path, include

from apps.administrador.views import index, listado_bienes, bienes_adjudicar, bienes_adjudicados, \
actualizar_bienes, eliminar_bienes, activar_permisos, actualizar_permiso

urlpatterns = [
    path('', index, name="administrador_index"),
    path('listado_bienes/', listado_bienes, name="listado_bienes"),
    path('bienes_adjudicar/<int:id_bien>/', bienes_adjudicar, name="adjudicion_bienes"),
    path('bienes_adjudicados/', bienes_adjudicados, name="bienes_adjudicados"),
    path('actualizar_bienes/<int:id_bien>/', actualizar_bienes, name="actualizacion_bienes"),
    path('eliminar_bienes/<int:id_bien>/', eliminar_bienes, name="eliminacion_bienes"),
    path('permisos/', activar_permisos, name="asignar_permisos"),
    path('permisos/envio/', actualizar_permiso, name="actualizar_permiso"),
]
