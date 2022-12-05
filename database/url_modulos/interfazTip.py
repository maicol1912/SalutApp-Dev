from django.urls import path
from database.views.interfazUsuario import ITip

app_name = "ITip"
urlpatterns = [
    path('listar/',ITip.listar,name="listar")
]