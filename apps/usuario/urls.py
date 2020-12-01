from django.urls import path, include

from apps.usuario.views import index, bienes_insert, bienes_list, bienes_update, bienes_delete, bienes_verificados

urlpatterns = [
    path('', index, name="usuario_index"),
    path('insert_bienes/', bienes_insert, name="insertar_bienes"),
    path('list_bienes/', bienes_list, name="listar_bienes"),
    path('update_bienes/<int:id_bien>/', bienes_update, name="editar_bienes"),
    path('delete_bienes/<int:id_bien>/', bienes_delete, name="eliminar_bienes"),
    path('bienes_verificados/', bienes_verificados, name="bienes_verificados"),
]