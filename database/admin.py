from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass
