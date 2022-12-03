from django.urls import path
from database.views.interfazUsuario import ITarea

app_name = "ITarea"
urlpatterns = [
    path('formulario/', ITarea.formulario, name="formulario"),
    path('ingresar/', ITarea.ingresar, name="ingresar"),
    path('listar/',ITarea.listar,name="listar"),
    path('finalizar/',ITarea.finalizar,name="finalizar")
]
