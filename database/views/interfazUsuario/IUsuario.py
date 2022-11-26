from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Usuario
from django.contrib import messages
from datetime import datetime
from database.views.encriptacion import encriptador


# Create your views here.
def listar(request):
    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
        usuarioE = Usuario.objects.get(pk=request.session["logueo"][2])

        imc = (usuarioE.usuario_peso/(usuarioE.usuario_altura /
               100 * usuarioE.usuario_altura/100))
        imcFormateado = ("%.1f" % imc)
        print(usuarioE)
        context = {"datos":usuarioE,"imc":imcFormateado}
        return render(request, 'database/interfaces/interfazUsuario/listarUsuario.html',context)
    else:
        messages.warning(request, "usted no ha enviado datos...")
        return("indexUsuario")

def formulario(request):
    """
    Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Usuario`.

    **Template:**

    :template:`database/interfaces/interfazUsuario/registrarUsuario.html`
    """
    return render(request, 'database/interfaces/interfazUsuario/registrarUsuario.html')
    

def ingresar(request):
    """
    Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Usuario`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido
    """
    try:
        if request.method == "POST":
                altura = int(request.POST["usuario_altura"])
                peso = int(request.POST["usuario_peso"])
                edad = int(request.POST["usuario_edad"])
                if altura > 140 and peso > 40 and edad>=15:
                    password = request.POST["usuario_password"]
                    user = request.POST["usuario_nombre"]
                    correo = request.POST["usuario_correo"]
                    id = request.POST["usuario_id"]
                    if (Usuario.objects.filter(usuario_nombre=user) or Usuario.objects.filter(usuario_correo=correo) or Usuario.objects.filter(usuario_id=id)):
                        messages.warning(request, "Este usuario o correo ya esta en uso")
                        return redirect("indexUsuario")
                    else:
                        passwordEncriptado = encriptador.encriptarPassword(password)
                        fechaIngreso = datetime.strftime(datetime.now(), "%d-%m-%Y")
                        usuario = Usuario(usuario_id=request.POST["usuario_id"],
                                        usuario_nombre = user,
                                        usuario_correo = correo,
                                        usuario_password =passwordEncriptado ,
                                        usuario_peso = peso,
                                        usuario_altura = altura,
                                        usuario_edad = edad,
                                        usuario_rol = request.POST["usuario_rol"],
                                        usuario_nro_semanas=0,
                                        usuario_fecha_avance=fechaIngreso,
                                        usuario_nro_tarea = 0
                                )
                        usuario.save()
                        messages.success(request, "Usuario guardado Correctamente")
                else:
                    messages.warning(request, "Los datos que ingresaste no son validos")
        else:
            messages.warning(request, "usted no ha enviado datos...")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('IMeta:formulario')
    


def encontrar(request):
    """
    Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Usuario`.

    **Template:**

    :template:`database/usuario/actualizarUsuario.html`
    """
    if request.session["logueo"][1] == "admin" or request.session["logueo"][1] == "usuario":
        usuario = Usuario.objects.get(pk=request.session["logueo"][2])
        context = {"datos": usuario}
        return render(request, "database/interfaces/interfazUsuario/actualizarUsuario.html", context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def actualizar(request): 
    """
    Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Usuario`. si todo esta correcto
    """
    if request.session["logueo"][1] == "admin" or request.session["logueo"][1] == "usuario":
        id = request.session["logueo"][2]
        password = request.POST["usuario_password"]
        passwordEncriptado = encriptador.encriptarPassword(password)

        usuarioActualizar = Usuario.objects.get(pk=id)
        usuarioActualizar.usuario_id = id
        usuarioActualizar.usuario_nombre = request.POST["usuario_nombre"]
        usuarioActualizar.usuario_correo = request.POST["usuario_correo"]
        usuarioActualizar.usuario_password = passwordEncriptado
        usuarioActualizar.save()
        return redirect('IUsuario:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("indexUsuario")
