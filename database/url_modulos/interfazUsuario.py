from django.urls import path
from database.views.interfazUsuario import IUsuario

app_name = "IUsuario"
urlpatterns = [
    path('listar/', IUsuario.listar, name="listar"),
    path('formulario/', IUsuario.formulario, name="formulario"),
    path('ingresar/', IUsuario.ingresar, name="ingresar"),
    path('encontrar/', IUsuario.encontrar, name="encontrar"),
    path('actualizar/', IUsuario.actualizar, name="actualizar"),
]