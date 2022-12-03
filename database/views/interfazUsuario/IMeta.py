from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Usuario,Meta
from django.contrib import messages
from database.views.encriptacion import encriptador

def listar(request):
    """Lista la meta designada de :model: `database.Meta` para el cliente :model: `database.Usuario`

    Args:
        q: ninguno

    Returns:
        template:`database/interfaces/interfazMeta/listarMeta.html`
    """
    idUsuario = request.session["logueo"][2]
    
    if Meta.objects.filter(usuario_id=idUsuario):
        metaE = Meta.objects.filter(usuario_id=idUsuario)
        context = {"meta":metaE[0]}
        return render(request, 'database/interfaces/interfazMeta/listarMeta.html', context)
    else:
        return redirect("IMeta:formulario")


def formulario(request):
    """Renderiza el formulario para que el cliente :model: `database.Usuario` ingrese 
    la infromacion necesaria para crear una meta`

    Args:
        q: ninguno

    Returns:
        template:`database/interfaces/interfazMeta/registrarMeta.html`
    """
    return render(request, 'database/interfaces/interfazMeta/registrarMeta.html')


def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Meta` 

    Args:
        q: ninguno

    Returns:
        nada
    """
    try:
        if request.method == "POST":
            usuarioP = request.POST["meta_usuario"]
            usuario = Usuario.objects.get(pk=usuarioP)
            usuarioE = Usuario.objects.get(pk=request.session["logueo"][2])
            altura = usuarioE.usuario_altura / 100
            peso = usuarioE.usuario_peso
            imc = (peso/(altura * altura))
        
            tipoMeta = request.POST["meta_tipo"]

            pesoIdeal = int(request.POST["meta_peso"])
            imcIdeal = (pesoIdeal/(altura * altura))
            
            if imc <=18.4 and tipoMeta == "bajar peso":
                messages.warning(request, "su peso es bajo, no puede bajar mas peso")
                return ("indexUsuario")
                
            if imc >24.9 and tipoMeta == "subir peso":
                messages.warning(request, "su peso es alto, no puede subir mas peso")
                return ("indexUsuario")

            if imcIdeal < 24.9 and imcIdeal >18.9:
                if tipoMeta == "bajar peso":
                    if usuarioE.usuario_peso - 5 > pesoIdeal:
                        messages.warning(request, "esta meta no es saludable, esta fuera de los pesos recomendables")
                        return redirect("indexUsuario")

                if tipoMeta == "subir peso":
                    if usuarioE.usuario_peso + 5 < pesoIdeal:
                        messages.warning(
                            request, "esta meta no es saludable, esta fuera de los pesos recomendables")
                        return redirect("indexUsuario")
            if tipoMeta == "recomposicion" and pesoIdeal != usuarioE.usuario_peso:
                messages.warning(
                    request, "no estas entrando en recomposicion")
                return redirect("indexUsuario")
            
                
                
            meta = Meta(meta_tipo=tipoMeta,
                        meta_desc=request.POST["meta_desc"],
                        meta_peso_ideal=pesoIdeal,
                        usuario_id=usuario
                        )
            meta.save()
            messages.success(request, "Meta guardada Correctamente")
        else:
            messages.warning(request, "usted no ha enviado datos...")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('IPlan:ingresar')
    
