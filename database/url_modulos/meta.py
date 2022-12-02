from django.urls import path
from database.views import meta

app_name = "meta"
urlpatterns = [
    path('listar/', meta.listar, name="listar"),
    path('formulario/', meta.formulario, name="formulario"),
    path('ingresar/', meta.ingresar, name="ingresar"),
    path('eliminar/<id>/', meta.eliminar, name="eliminar"),
    path('encontrar/<id>/', meta.encontrar, name="encontrar"),
    path('actualizar/', meta.actualizar, name="actualizar"),
    path('buscar/', meta.buscar, name="buscar")
]
