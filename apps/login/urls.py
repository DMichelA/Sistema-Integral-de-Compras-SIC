from django.urls import path, include

from apps.login.views import login, login_success

urlpatterns = [
    path('', login, name="login"),
    #path('', logout, name="logout"),
    path('login_success/', login_success, name="login_success"),

]