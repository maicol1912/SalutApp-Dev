from django.urls import path
from database.views.interfazUsuario import IEspecificacion

app_name = "IEspecificacion"
urlpatterns = [
    path('listar/', IEspecificacion.listar, name="listar"),
]