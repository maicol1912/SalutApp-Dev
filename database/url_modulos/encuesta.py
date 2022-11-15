from django.urls import path
from database.views import encuesta

app_name = "encuesta"
urlpatterns = [
    path('listar/', encuesta.listar, name="listar"),
    path('formulario/', encuesta.formulario, name="formulario"),
    path('ingresar/', encuesta.ingresar, name="ingresar"),
    path('eliminar/<id>/', encuesta.eliminar, name="eliminar"),
    path('encontrar/<id>/', encuesta.encontrar, name="encontrar"),
    path('actualizar/', encuesta.actualizar, name="actualizar"),
    path('buscar/', encuesta.buscar, name="buscar")
]
