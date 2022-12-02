from django.urls import path
from database.views.interfazUsuario import IPlan

app_name = "IPlan"
urlpatterns = [
    path('listar/', IPlan.listar, name="listar"),
    path('ingresar/', IPlan.ingresar, name="ingresar"),
]
