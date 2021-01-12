from django.contrib import admin

# Register your models here.
from apps.requisicion.models import Requisicion, Requisicion_Bienes


admin.site.register(Requisicion)
admin.site.register(Requisicion_Bienes)