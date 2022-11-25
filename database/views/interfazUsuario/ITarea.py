from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Tarea, Usuario, Plan, Especificacion
from django.contrib import messages
from datetime import datetime, timedelta

# Create your views here.
nroMesTarea = None
def listar(request):
    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
        if Tarea.objects.filter(usuario_id=request.session["logueo"][2]):
            tarea = Tarea.objects.filter(
                usuario_id=request.session["logueo"][2])[0]
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
    try:
        if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
            print("entre al 1")
            usuario = Usuario.objects.get(pk=request.session["logueo"][2])
            if Plan.objects.filter(usuario_id=request.session["logueo"][2]):
                plan = Plan.objects.filter(usuario_id=request.session["logueo"][2])[0]
                especificacion = Especificacion.objects.get(pk=plan.especificacion_id.especificacion_id)
                nroIdTareaAcum = 0
                print("-1--------------------------------------")
                print(f"nroMesTarea: {nroMesTarea}")
                print(f"nroIdTarea: {nroIdTareaAcum}")
                print("-*--------------------------------------")
                if nroMesTarea < 4:
                    tareaId = str(usuario.usuario_id) + str(nroIdTareaAcum)
                    print("-*--------------------------------------")
                    print(tareaId)
                    print("-*--------------------------------------")
                if nroMesTarea >=4:
                    nroIdTareaAcum =+1
                    tareaId = str(usuario.usuario_id) + str(nroIdTareaAcum)
                    nroMesTarea = 0
                    print("-*--------------------------------------")
                    print(tareaId)
                    print("-*--------------------------------------")
                if nroMesTarea == 0:
                    
                    tarea = Tarea(tarea_id=tareaId,
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
                    tarea.save()
                    print("-*--------------------------------------")
                    print(request.POST["tarea_check"])
                    print(request.POST["nuevo_peso"])
                    print("-*--------------------------------------")
                    nroMesTarea =1
                    messages.warning(request, "Guardamos tu avance con exito")
                    return redirect("usuarioIndex")
                if nroMesTarea == 1:

                    tarea = Tarea(tarea_id=tareaId,
                                    tarea_check_2=request.POST["tarea_check"],
                                    peso_check_2=request.POST["nuevo_peso"],
                                    tarea_check_3=None,
                                    peso_check_3=None,
                                    tarea_check_4=None,
                                    peso_check_4=None,
                                especificacion_id=especificacion,
                                usuario_id=usuario)
                    tarea.save()
                    nroMesTarea =2
                    messages.warning(request, "Guardamos tu avance con exito")
                    return redirect("usuarioIndex")
                
                if nroMesTarea == 2:

                    tarea = Tarea(tarea_id=tareaId,
                                    tarea_check_3=request.POST["tarea_check"],
                                    peso_check_3=request.POST["nuevo_peso"],
                                    tarea_check_4=None,
                                    peso_check_4=None,
                                especificacion_id=especificacion,
                                usuario_id=usuario)
                    tarea.save()
                    nroMesTarea =3
                    messages.warning(request, "Guardamos tu avance con exito")
                    return redirect("usuarioIndex")
                if nroMesTarea == 3:

                    tarea = Tarea(tarea_id=tareaId,
                                    tarea_check_4=request.POST["tarea_check"],
                                    peso_check_4=request.POST["nuevo_peso"],
                                especificacion_id=especificacion,
                                usuario_id=usuario)
                    tarea.save()
                    nroMesTarea =4
                    messages.warning(request, "Guardamos tu avance con exito")
                    return redirect("usuarioIndex")
            else:
                messages.warning(request, " No Encontramos Planes para ti")
                return redirect("IPlan:listar")
        else:
            messages.warning(request, " No Encontramos tareas para ti")
            return redirect("indexUsuario")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('IPlan:ingresar')
