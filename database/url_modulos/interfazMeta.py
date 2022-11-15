from django.urls import path
from database.views.interfazUsuario import IMeta

app_name = "IMeta"
urlpatterns = [
    path('listar/', IMeta.listar, name="listar"),
    path('formulario/', IMeta.formulario, name="formulario"),
    path('ingresar/', IMeta.ingresar, name="ingresar"),
]