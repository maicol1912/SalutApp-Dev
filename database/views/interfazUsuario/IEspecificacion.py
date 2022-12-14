from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Especificacion,Plan,Meta,Usuario
from django.contrib import messages

def listar(request):
    """Lista las especificaciones existentes en :model: `database.Especificacion` para el cliente :model: `database.Usuario`

    Args:
        q: ninguno

    Returns:
        template:`database/interfaces/interfazEspecificacion/listarEspecificacion.html`
    """ 
    try:
        if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
            if Meta.objects.filter(usuario_id = request.session["logueo"][2]):
                if Plan.objects.filter(usuario_id = request.session["logueo"][2]):
                    planE = Plan.objects.filter(usuario_id = request.session["logueo"][2])[0]
                    especificacion = Especificacion.objects.get(pk=planE.especificacion_id.especificacion_id)
                    context = {"datos": especificacion}
                    return render(request, 'database/interfaces/interfazEspecificacion/listarEspecificacion.html', context)
                else:
                    return redirect("IPlan:listar")
            else:
                return redirect("IMeta:formulario")
        else:
            messages.warning(request, " No tienes acceso a este modulo")
            return redirect("indexUsuario")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")

