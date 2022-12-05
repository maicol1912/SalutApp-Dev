from django.urls import path
from database.views import pqr

app_name = "pqr"
urlpatterns = [
    path('listar/', pqr.listar, name="listar"),
    path('formulario/', pqr.formulario, name="formulario"),
    path('ingresar/', pqr.ingresar, name="ingresar"),
    path('eliminar/<id>/', pqr.eliminar, name="eliminar"),
    path('encontrar/<id>/', pqr.encontrar, name="encontrar"),
    path('actualizar/', pqr.actualizar, name="actualizar"),
    path('buscar/', pqr.buscar, name="buscar")
]
