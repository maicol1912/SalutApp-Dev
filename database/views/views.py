from django.shortcuts import render,redirect
# Mensajes tipo cookie temporales
from django.contrib import messages
from ..models import Usuario
from database.views.encriptacion.encriptador import *

# Create your views here.

def index(request):
    """
    Renderiza un template de inicio dependiendo el tipo de usuario de :model: `database.`

    **Template:**

    """
    return render(request, 'database/index.html')

def indexUsuario(request):
    """
    Renderiza un template de inicio dependiendo el tipo de usuario de :model: `database.`

    **Template:**

    """
    return render(request, 'database/indexUsuario.html')

def landing(request):
    """
    Renderiza un template de inicio para todos los tipos de usuario.
    **Template:**

    """
    return render(request, 'database/landing.html')



