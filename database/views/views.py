from django.shortcuts import render,redirect
# Mensajes tipo cookie temporales
from django.contrib import messages
from ..models import Usuario
from database.views.encriptacion.encriptador import *

# Create your views here.

def index(request):
    return render(request, 'database/index.html')

def indexUsuario(request):
    return render(request, 'database/indexUsuario.html')

def landing(request):
    return render(request, 'database/landing.html')



