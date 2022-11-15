from django.urls import path
from database.views import especificacion

app_name = "especificacion"
urlpatterns = [
    path('listar/', especificacion.listar, name="listar"),
    path('formulario/', especificacion.formulario, name="formulario"),
    path('ingresar/', especificacion.ingresar, name="ingresar"),
    path('eliminar/<id>/', especificacion.eliminar, name="eliminar"),
    path('encontrar/<id>/', especificacion.encontrar, name="encontrar"),
    path('actualizar/', especificacion.actualizar, name="actualizar"),
    path('buscar/', especificacion.buscar, name="buscar")
]
