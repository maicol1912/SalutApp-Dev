from django.urls import path
from database.views import usuario_encuesta

app_name = "usuarioEncuesta"
urlpatterns = [
    path('listar/', usuario_encuesta.listar, name="listar"),
    path('formulario/', usuario_encuesta.formulario, name="formulario"),
    path('ingresar/', usuario_encuesta.ingresar, name="ingresar"),
    path('eliminar/<id>/', usuario_encuesta.eliminar, name="eliminar"),
    path('encontrar/<id>/', usuario_encuesta.encontrar, name="encontrar"),
    path('actualizar/', usuario_encuesta.actualizar, name="actualizar"),
    path('buscar/', usuario_encuesta.buscar, name="buscar")
]
