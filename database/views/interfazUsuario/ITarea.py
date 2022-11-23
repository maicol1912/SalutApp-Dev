from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Tarea, Usuario
from django.contrib import messages
from datetime import datetime, timedelta


# Create your views here.

def listar(request):
    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
        if Tarea.objects.filter(usuario_id=request.session["logueo"][2]):
            tarea = Tarea.objects.filter(usuario_id = request.session["logueo"][2])[0]
            context = {"datos": tarea}
            return render(request, 'database/interfaces/interfazTarea/listarTarea.html', context)
        else:
            return redirect("ITarea:formulario")
    else:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")


def formulario(request):
    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
        fechaActual = datetime.now()
        fechaUsuario=datetime.strptime(request.session["logueo"][3], "%d-%m-%Y")

        diferenciaFecha = fechaActual - timedelta(days=7)

        if diferenciaFecha >= fechaUsuario:
            return render(request, 'database/interfaces/interfazTarea/registrarTarea.html')
        else:
            messages.warning(request, "No han pasado los suficientes dias para marcar como realizada una tarea")
            return redirect("indexUsuario")

    else:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")
    


def ingresar(request):
    try:
        if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
            usuario = Usuario.objects.get(pk=request.session["logueo"][2])
            pqr = Pqr(pqr_tipo=request.POST["pqr_tipo"],
                      pqr_desc=request.POST["pqr_desc"],
                      usuario_id=usuario)
            pqr.save()
            messages.warning(
                request, "Gracias por enviar tu aporte en breves recibiras novedades")
            return redirect("indexUsuario")

        else:
            messages.warning(request, " No tienes acceso a este modulo")
            return redirect("indexUsuario")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('IPlan:ingresar')
