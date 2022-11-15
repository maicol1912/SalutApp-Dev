from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Usuario,Meta
from django.contrib import messages
from database.views.encriptacion import encriptador


# Create your views here.

def listar(request):
    idUsuario = request.session["logueo"][2]
    
    if Meta.objects.filter(usuario_id=idUsuario):
        metaE = Meta.objects.filter(usuario_id=idUsuario)
        context = {"meta":metaE[0]}
        return render(request, 'database/interfaces/interfazMeta/listarMeta.html', context)
    else:
        return redirect("IMeta:formulario")


def formulario(request):
        return render(request, 'database/interfaces/interfazMeta/registrarMeta.html')


def ingresar(request):
    try:
        if request.method == "POST":
            usuarioP = request.POST["meta_usuario"]
            usuario = Usuario.objects.get(pk=usuarioP)

            meta = Meta(meta_tipo=request.POST["meta_tipo"],
                        meta_desc=request.POST["meta_desc"],
                        meta_peso_ideal=float(request.POST["meta_peso"]),
                        usuario_id=usuario
                        )
            meta.save()
            messages.success(request, "Meta guardada Correctamente")
        else:
            messages.warning(request, "usted no ha enviado datos...")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('IMeta:listar')
    
