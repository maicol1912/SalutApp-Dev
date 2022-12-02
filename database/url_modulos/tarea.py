from django.urls import path
from database.views import tarea

app_name = "tarea"
urlpatterns = [
    path('listar/', tarea.listar, name="listar"),
    path('formulario/', tarea.formulario, name="formulario"),
    path('ingresar/', tarea.ingresar, name="ingresar"),
    path('eliminar/<id>/', tarea.eliminar, name="eliminar"),
    path('encontrar/<id>/', tarea.encontrar, name="encontrar"),
    path('actualizar/', tarea.actualizar, name="actualizar"),
    path('buscar/', tarea.buscar, name="buscar")
]
