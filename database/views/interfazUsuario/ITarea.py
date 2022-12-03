from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Tarea, Usuario, Plan, Especificacion,Meta
from django.contrib import messages
from datetime import datetime, timedelta

# Create your views here.

def listar(request):
    """Lista las tareas :model: `database.Tarea` disponibles para el usuario :model: `database.Usuario` en el template

    Args:
        q: ninguno

    Returns:
        template:`database/interfaces/interfazTarea/listarTarea.html`
    """

    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
        if Tarea.objects.filter(usuario_id=request.session["logueo"][2]):
            tarea = Tarea.objects.filter(usuario_id=request.session["logueo"][2])
            
            context = {"datos": tarea,}
            return render(request, 'database/interfaces/interfazTarea/listarTarea.html', context)
        else:
            return redirect("ITarea:formulario")
    else:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")


def formulario(request):
    """Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Tarea`.

    Args:
        q: ninguno

    Returns:
        template:`database/interfaces/interfazTarea/registrarTarea.html`
    """

    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
        fechaActual = datetime.now()
        usuario = Usuario.objects.get(pk=request.session["logueo"][2])
        fechaUsuario = datetime.strptime(usuario.usuario_fecha_avance, "%d-%m-%Y")

        diferenciaFecha = fechaActual - timedelta(days=7)

        #if diferenciaFecha >= fechaUsuario:

        context = {"semana":usuario.usuario_nro_semanas}
        return render(request, 'database/interfaces/interfazTarea/registrarTarea.html',context)
        #else:
            #messages.warning(request, "No han pasado los suficientes dias para marcar como realizada una tarea")
            #return redirect("indexUsuario")

    else:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")


def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a: model: `database.Tarea`

    Args:
        q: ninguno

    Returns:
        nada
    """

    try:
        if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
            usuario = Usuario.objects.get(pk=request.session["logueo"][2])
            if Plan.objects.filter(usuario_id=request.session["logueo"][2]):
                plan = Plan.objects.filter(usuario_id=request.session["logueo"][2])[0]
                especificacion = Especificacion.objects.get(pk=plan.especificacion_id.especificacion_id)
                    
                if usuario.usuario_nro_semanas == 0:
                    tareaId = str(request.session["logueo"][2]) + str(usuario.usuario_nro_tarea)
                    tareaCreada = Tarea(
                                tarea_id=tareaId,
                                tarea_check_1=request.POST["tarea_check"],
                                peso_check_1=request.POST["nuevo_peso"],
                                tarea_check_2=None,
                                peso_check_2=None,
                                tarea_check_3=None,
                                peso_check_3=None,
                                tarea_check_4=None,
                                peso_check_4=None,
                                especificacion_id=especificacion,
                                usuario_id=usuario)
                    tipoMeta = Meta.objects.filter(usuario_id=request.session["logueo"][2])[0].meta_tipo
                    pesoMeta = Meta.objects.filter(usuario_id=request.session["logueo"][2])[0].meta_peso_ideal
                    if  tipoMeta== "subir peso" and Usuario.objects.get(pk=request.session["logueo"][2]).usuario_peso > int(request.POST["nuevo_peso"]):
                        messages.warning(request, "Tu peso no es verdadero, no haz llevado bien tu dieta")
                        return redirect("indexUsuario")
                    if  tipoMeta == "bajar peso" and Usuario.objects.get(pk=request.session["logueo"][2]).usuario_peso < int(request.POST["nuevo_peso"]):
                        messages.warning(request, "Tu peso no es verdadero, no haz llevado bien tu dieta")
                        return redirect("indexUsuario")
                    if tipoMeta == "subir peso" and int(request.POST["nuevo_peso"]) >= pesoMeta:
                        return redirect("ITarea:finalizar")
                    if tipoMeta == "bajar peso" and int(request.POST["nuevo_peso"]) <= pesoMeta:
                        return redirect("ITarea:finalizar")


                    tareaCreada.save()
                    usuario.usuario_fecha_avance = datetime.strftime(datetime.now(), "%d-%m-%Y")
                    usuario.usuario_nro_semanas = 1
                    usuario.save()
                    messages.warning(request, "Guardamos tu avance con exito")
                    return redirect("indexUsuario")
                if usuario.usuario_nro_semanas == 1:
                    tareaEncontrada = Tarea.objects.filter(usuario_id=request.session["logueo"][2])[0]
                    tareaEncontrada.tarea_check_2 = request.POST["tarea_check"]
                    tareaEncontrada.peso_check_2 = request.POST["nuevo_peso"]
                    
                    tipoMeta = Meta.objects.filter(
                        usuario_id=request.session["logueo"][2])[0].meta_tipo
                    pesoMeta = Meta.objects.filter(usuario_id=request.session["logueo"][2])[
                        0].meta_peso_ideal
                    if tipoMeta == "subir peso" and Usuario.objects.get(pk=request.session["logueo"][2]).usuario_peso > request.POST["nuevo_peso"]:
                        messages.warning(
                            request, "Tu peso no es verdadero, no haz llevado bien tu dieta")
                        return redirect("indexUsuario")
                    if tipoMeta == "bajar peso" and Usuario.objects.get(pk=request.session["logueo"][2]).usuario_peso < request.POST["nuevo_peso"]:
                        messages.warning(
                            request, "Tu peso no es verdadero, no haz llevado bien tu dieta")
                        return redirect("indexUsuario")
                    if tipoMeta == "subir peso" and int(request.POST["nuevo_peso"]) >= pesoMeta:
                        return redirect("ITarea:finalizar")
                    if tipoMeta == "bajar peso" and int(request.POST["nuevo_peso"]) <= pesoMeta:
                        return redirect("ITarea:finalizar")

                    tareaEncontrada.save()
                    usuario.usuario_fecha_avance = datetime.strftime(datetime.now(), "%d-%m-%Y")
                    usuario.usuario_nro_semanas = 2
                    usuario.save()
                    messages.warning(request, "Guardamos tu avance con exito")
                    return redirect("indexUsuario")
                
                if usuario.usuario_nro_semanas == 2:
                    tareaEncontrada = Tarea.objects.filter(usuario_id=request.session["logueo"][2])[0]
                    tareaEncontrada.tarea_check_3 = request.POST["tarea_check"]
                    tareaEncontrada.peso_check_3 = request.POST["nuevo_peso"]
                    
                    tipoMeta = Meta.objects.filter(
                        usuario_id=request.session["logueo"][2])[0].meta_tipo
                    pesoMeta = Meta.objects.filter(usuario_id=request.session["logueo"][2])[
                        0].meta_peso_ideal
                    if tipoMeta == "subir peso" and Usuario.objects.get(pk=request.session["logueo"][2]).usuario_peso > request.POST["nuevo_peso"]:
                        messages.warning(
                            request, "Tu peso no es verdadero, no haz llevado bien tu dieta")
                        return redirect("indexUsuario")
                    if tipoMeta == "bajar peso" and Usuario.objects.get(pk=request.session["logueo"][2]).usuario_peso < request.POST["nuevo_peso"]:
                        messages.warning(
                            request, "Tu peso no es verdadero, no haz llevado bien tu dieta")
                        return redirect("indexUsuario")
                    if tipoMeta == "subir peso" and int(request.POST["nuevo_peso"]) >= pesoMeta:
                        return redirect("ITarea:finalizar")
                    if tipoMeta == "bajar peso" and int(request.POST["nuevo_peso"]) <= pesoMeta:
                        return redirect("ITarea:finalizar")

                    tareaEncontrada.save()
                    usuario.usuario_fecha_avance = datetime.strftime(datetime.now(), "%d-%m-%Y")
                    usuario.usuario_nro_semanas = 3
                    usuario.save()
                    messages.warning(request, "Guardamos tu avance con exito")
                    return redirect("indexUsuario")
                if usuario.usuario_nro_semanas == 3:
                    tareaEncontrada = Tarea.objects.filter(usuario_id=request.session["logueo"][2])[0]
                    tareaEncontrada.tarea_check_4 = request.POST["tarea_check"]
                    tareaEncontrada.peso_check_4 = request.POST["nuevo_peso"]

                    tipoMeta = Meta.objects.filter(
                        usuario_id=request.session["logueo"][2])[0].meta_tipo
                    pesoMeta = Meta.objects.filter(usuario_id=request.session["logueo"][2])[
                        0].meta_peso_ideal
                    if tipoMeta == "subir peso" and Usuario.objects.get(pk=request.session["logueo"][2]).usuario_peso > request.POST["nuevo_peso"]:
                        messages.warning(
                            request, "Tu peso no es verdadero, no haz llevado bien tu dieta")
                        return redirect("indexUsuario")
                    if tipoMeta == "bajar peso" and Usuario.objects.get(pk=request.session["logueo"][2]).usuario_peso < request.POST["nuevo_peso"]:
                        messages.warning(
                            request, "Tu peso no es verdadero, no haz llevado bien tu dieta")
                        return redirect("indexUsuario")
                    if tipoMeta == "subir peso" and int(request.POST["nuevo_peso"]) >= pesoMeta:
                        return redirect("ITarea:finalizar")
                    if tipoMeta == "bajar peso" and int(request.POST["nuevo_peso"]) <= pesoMeta:
                        return redirect("ITarea:finalizar")

                    tareaEncontrada.save()
                    usuario.usuario_fecha_avance = datetime.strftime(datetime.now(), "%d-%m-%Y")
                    usuario.usuario_nro_semanas = 0
                    usuario.usuario_nro_tarea += 1 
                    usuario.save()
                    messages.warning(request, "Guardamos tu avance con exito")
                    return redirect("indexUsuario")
            else:
                messages.warning(request, " No Encontramos Planes para ti")
                return redirect("IPlan:listar")
        else:
            messages.warning(request, " No Encontramos tareas para ti")
            return redirect("indexUsuario")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('indexUsuario')


def finalizar(request):
    user = Usuario.objects.get(pk=request.session["logueo"][2])
    user.delete()
    messages.warning(request, "LLegaste a tu meta de peso, si deseas seguir con otra dieta registrate con tus nuevos datos")
    return redirect('indexUsuario')

