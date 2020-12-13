from django.urls import path, include

from apps.login.views import login, login_success, accounterror

urlpatterns = [
    path('', login, name="login"),
    #path('', logout, name="logout"),
    path('login_success/', login_success, name="login_success"),
    path('accounts/login/', accounterror, name="accounterror"),

]