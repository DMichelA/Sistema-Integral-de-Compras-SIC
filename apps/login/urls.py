from django.urls import path, include

from apps.login.views import login

urlpatterns = [
    path('', login, name="login"),
]