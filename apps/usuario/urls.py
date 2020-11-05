from django.urls import path, include

from apps.usuario.views import index

urlpatterns = [
    path('', index, name="index"),
]