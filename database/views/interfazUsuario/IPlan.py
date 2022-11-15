from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Usuario,Meta,Plan
from django.contrib import messages


# Create your views here.
def listar(request):
    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":

        usuarioE = Usuario.objects.get(pk=request.session["logueo"][2])
        altura = usuarioE.usuario_altura / 100
        peso = usuarioE.usuario_peso 
        imc = (usuarioE.usuario_peso/(usuarioE.usuario_altura /100 * usuarioE.usuario_altura/100))
        imcFormateado = ("%.1f"%imc)
        
        context = {"datos": usuarioE}
        return render(request, 'database/interfaces/interfazUsuario/listarUsuario.html', context)
    else:
        messages.warning(request, "usted no ha enviado datos...")
        return ("indexUsuario")



def ingresar(request):
    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
        idUsuario = request.session["logueo"][2]
        if (Usuario.objects.get(pk=id) and Meta.objects.filter(id_usuario = idUsuario)):
            usuario = Usuario.objects.get(pk=id)
            imc = (usuario.usuario_peso/((usuario.usuario_altura/100) * (usuario.usuario_altura/100)))
            meta = Meta.objects.filter(id_usuario=idUsuario)[0]
            if(imc<=15):
                textoDelgadezExtrema = "Lo que debes realizar es un superavit calorico agresivo ya que estas muy por debajo del peso deseado"
                recomendacionesDelgadezExtrema = "debes realizar ejercicios de hipertrofia, comer mas veces al dia ademas subir mucho el numero de calorias que ingieres"
                plan = Plan(plan_desc=textoDelgadezExtrema,
                            plan_recomendaciones=recomendacionesDelgadezExtrema,
                            especificacion_id=1,
                            meta_id=meta,
                            usuario_id=usuario )
    else:
        messages.warning(request, "usted no ha enviado datos...")
        return ("indexUsuario")
