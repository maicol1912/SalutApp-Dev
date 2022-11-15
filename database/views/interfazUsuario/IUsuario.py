from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Usuario
from django.contrib import messages
from database.views.encriptacion import encriptador


# Create your views here.

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
                password = request.POST["usuario_password"]
                user = request.POST["usuario_nombre"]
                correo = request.POST["usuario_correo"]
                if (Usuario.objects.filter(usuario_nombre = user) or Usuario.objects.filter(usuario_nombre = user)):
                    messages.warning(request, "Este usuario o correo ya esta en uso")
                    return redirect("indexUsuario")
                else:
                    passwordEncriptado = encriptador.encriptarPassword(password)
                    usuario = Usuario(usuario_id=request.POST["usuario_id"],
                                    usuario_nombre = user,
                                    usuario_correo = correo,
                                    usuario_password =passwordEncriptado ,
                                    usuario_peso = float(request.POST["usuario_peso"]),
                                    usuario_altura = int(request.POST["usuario_altura"]),
                                    usuario_edad = int(request.POST["usuario_edad"]),
                                    usuario_rol = request.POST["usuario_rol"]
                            )
                    usuario.save()
                    messages.success(request, "Usuario guardado Correctamente")
        else:
            messages.warning(request, "usted no ha enviado datos...")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('indexUsuario')
    


def encontrar(request, id):
    """
    Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Usuario`.

    **Template:**

    :template:`database/usuario/actualizarUsuario.html`
    """
    if request.session["logueo"][1] =="admin":
        usuario = Usuario.objects.get(pk=id)
        context = {"datos": usuario}
        return render(request, "database/usuario/actualizarUsuario.html", context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def actualizar(request): 
    """
    Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Usuario`. si todo esta correcto
    """
    if request.session["logueo"][1] =="admin":
        id = request.POST["id"]
        password = request.POST["usuario_password"]
        passwordEncriptado = encriptador.encriptarPassword(password)

        usuario = Usuario.objects.get(pk=id)
        usuario.usuario_id = id
        usuario.usuario_nombre = request.POST["usuario_nombre"]
        usuario.usuario_correo = request.POST["usuario_correo"]
        usuario.usuario_password = passwordEncriptado
        usuario.usuario_peso = float(request.POST["usuario_peso"])
        usuario.usuario_altura = int(request.POST["usuario_altura"])
        usuario.usuario_edad = int(request.POST["usuario_edad"])
        usuario.usuario_rol = request.POST["usuario_rol"]
        usuario.save()
        return redirect('usuario:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")