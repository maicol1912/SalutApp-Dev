from django.urls import path
from database.views.interfazUsuario import IMeta

app_name = "IMeta"
urlpatterns = [
    path('formulario/', IMeta.formulario, name="formulario"),
    path('ingresar/', IMeta.ingresar, name="ingresar"),
    path('encontrar/<id>/', IMeta.encontrar, name="encontrar"),
    path('actualizar/', IMeta.actualizar, name="actualizar"),
]