from django.urls import path, include

from apps.administrador.views import index

urlpatterns = [
    path('', index, name="index"),
]