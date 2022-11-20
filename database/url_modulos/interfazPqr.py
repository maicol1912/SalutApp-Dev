from django.urls import path
from database.views.interfazUsuario import IPqr

app_name = "IPqr"
urlpatterns = [
    path('formulario/', IPqr.formulario, name="formulario"),
    path('ingresar/', IPqr.ingresar, name="ingresar"),
]