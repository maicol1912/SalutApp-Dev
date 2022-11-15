from django.urls import path
from database.views import usuario

app_name = "usuario"
urlpatterns = [
    path('listar/', usuario.listar, name="listar"),
    path('formulario/', usuario.formulario, name="formulario"),
    path('ingresar/', usuario.ingresar, name="ingresar"),
    path('eliminar/<id>/', usuario.eliminar, name="eliminar"),
    path('encontrar/<id>/', usuario.encontrar, name="encontrar"),
    path('actualizar/', usuario.actualizar, name="actualizar"),
    path('buscar/', usuario.buscar, name="buscar")
]
