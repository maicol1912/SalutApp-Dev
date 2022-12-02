from django.urls import path
from database.views import plan

app_name = "plan"
urlpatterns = [
    path('listar/', plan.listar, name="listar"),
    path('formulario/', plan.formulario, name="formulario"),
    path('ingresar/', plan.ingresar, name="ingresar"),
    path('eliminar/<id>/', plan.eliminar, name="eliminar"),
    path('encontrar/<id>/', plan.encontrar, name="encontrar"),
    path('actualizar/', plan.actualizar, name="actualizar"),
    path('buscar/', plan.buscar, name="buscar")
]
