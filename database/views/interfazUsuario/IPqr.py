from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Pqr,Usuario
from django.contrib import messages
from database.views.encriptacion import encriptador


# Create your views here.

def formulario(request):
        return render(request, 'database/interfaces/interfazPqr/registrarPqr.html')


def ingresar(request):
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