
from django.contrib import admin
from apps.login.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'rol', 'area', 'created_at']


admin.site.register(User, UserAdmin)


# admin.site.register(User) funcional para la clase User 