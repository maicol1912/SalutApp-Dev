from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Usuario,Meta,Plan,Especificacion
from django.contrib import messages


# Create your views here.
def listar(request):
    """Lista el plan y las recomendaciones dadas para el cliente :model: `database.Usuario` en el template

    Args:
        q: ninguno

    Returns:
        template:`database/interfaces/interfazPlan/listarPlan.html`
        
    """
    try:
        if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
            usuario = Usuario.objects.get(pk=request.session["logueo"][2])
            if Meta.objects.filter(usuario_id=usuario):
                meta = Meta.objects.filter(usuario_id=usuario)[0]
                if Plan.objects.filter(meta_id=meta.id):
                
                    metaE = Meta.objects.filter(usuario_id = usuario)[0]
                    plan = Plan.objects.filter(meta_id = metaE.id)[0]
                
                    context = {"datos": plan}
                    return render(request, 'database/interfaces/interfazPlan/listarPlan.html', context)
                else:
                    return redirect("IPlan:ingresar")
            else:
                
                return redirect("IMeta:formulario")
        else:
            messages.warning(request, "usted no tiene acceso a este modulo")
            return redirect("indexUsuario")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")



def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a: model: `database.Plan`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido

    Args:
        q: ninguno

    Returns:
        nada 
    """
    try:
        if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
            idUsuario = request.session["logueo"][2]

            if (Usuario.objects.get(pk=idUsuario) and Meta.objects.filter(usuario_id=idUsuario)):
        
                usuario = Usuario.objects.get(pk=idUsuario)
                imc = (usuario.usuario_peso/((usuario.usuario_altura/100) * (usuario.usuario_altura/100)))
                
                meta = Meta.objects.filter(usuario_id=idUsuario)[0]
                
                if(meta.meta_tipo == "subir peso"):
                    textoBajoPeso = "Lo que debes realizar es un superavit calorico ya que estas  por debajo del peso deseado"
                    recomendacionesBajoPeso = "debes realizar ejercicios de hipertrofia, comer mas veces al dia ademas subir mucho el numero de calorias que ingieres"
                    especificacion = Especificacion.objects.get(pk='1131')

                    plan = Plan(plan_desc=textoBajoPeso,
                                plan_recomendaciones=recomendacionesBajoPeso,
                                especificacion_id=especificacion,
                                meta_id=meta,
                                usuario_id=usuario )
                    plan.save()
                    return redirect("IPlan:listar")

                if (meta.meta_tipo == "bajar peso"):
                    textoPesoAlto = "Lo que debes realizar es un deficit calorico ya que estas  por encima del peso deseado"
                    recomendacionesAltoPeso = "debes realizar ejercicios de hipertrofia pero lo debes acompañar con bastante cardio y ejercicios de vascularidad, comer 3 o 4 veces al dia ademas bajar el numero de calorias que consumes en un dia para entrar en un deficit calorico"
                    especificacion = Especificacion.objects.get(pk='1132')
                    plan = Plan(plan_desc=textoPesoAlto,
                                plan_recomendaciones=recomendacionesAltoPeso,
                                especificacion_id=especificacion,
                                meta_id=meta,
                                usuario_id=usuario)
                    plan.save()
                    return redirect("IPlan:listar")
                    
            else:
                messages.warning(request, "no has rellenado la meta")
                return redirect("IMeta:formulario")
        else:
            messages.warning(request, "No tienes acceso a este modulo")
            return redirect("indexUsuario")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")
