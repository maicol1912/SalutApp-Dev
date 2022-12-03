from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Pqr,Usuario
from django.contrib import messages
from database.views.encriptacion import encriptador


# Create your views here.

def formulario(request):
    """Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Pqr`.

    Args:
        q: ninguno

    Returns:
        template:`database/interfaces/interfazPqr/registrarPqr.html`
    """
    try:
        if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
            return render(request, 'database/interfaces/interfazPqr/registrarPqr.html')
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")

def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Pqr` 

    Args:
        q: ninguno

    Returns:
        nada
    """
    try:
        if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
            usuario = Usuario.objects.get(pk=request.session["logueo"][2])
            pqr = Pqr(pqr_tipo = request.POST["pqr_tipo"],
                      pqr_desc = request.POST["pqr_desc"],
                      usuario_id = usuario)
            pqr.save()
            messages.warning(request, "Gracias por enviar tu aporte en breves recibiras novedades")
            return redirect("indexUsuario")
            
        else:
            messages.warning(request, " No tienes acceso a este modulo")
            return redirect("indexUsuario")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('IPlan:ingresar')

    

