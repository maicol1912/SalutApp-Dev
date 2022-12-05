from django.urls import path
from database.views import tip

app_name = "tip"
urlpatterns = [
    path('listar/', tip.listar, name="listar"),
    path('formulario/', tip.formulario, name="formulario"),
    path('ingresar/', tip.ingresar, name="ingresar"),
    path('eliminar/<id>/', tip.eliminar, name="eliminar"),
    path('encontrar/<id>/', tip.encontrar, name="encontrar"),
    path('actualizar/', tip.actualizar, name="actualizar"),
    path('buscar/', tip.buscar, name="buscar")
]
