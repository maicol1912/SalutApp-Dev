from django.shortcuts import render,redirect
# Mensajes tipo cookie temporales
from django.contrib import messages
from ..models import Usuario
from database.views.encriptacion.encriptador import *

def loginFormulario(request):
    return render(request, 'database/login/login.html')  #Creo que aqui esta el error

def login(request):
    """
    Valida que los datos ingresados si forman parte de :model:`database.Usuario`.
    por lo tanto que si haya un usuario con esos datos
    """
    if request.method == "POST":
        try:
            user = request.POST["usuario"]
            passw = request.POST["clave"]
            usuarioObtenido = Usuario.objects.get(usuario_nombre = user)
            verificarContraseña = comparePassword(usuarioObtenido.usuario_password,passw)
            if (usuarioObtenido and verificarContraseña):
        
                # crear la sesión
                request.session["logueo"] = [usuarioObtenido.usuario_nombre, usuarioObtenido.usuario_rol, usuarioObtenido.usuario_id]
                if (request.session["logueo"][1] =="admin"):
                    messages.success(request, "Ha sido logueado con exito")
                    return redirect('index')   
                if (request.session["logueo"][1] =="usuario"):
                    messages.success(request, "Ha sido logueado con exito")
                    return redirect('indexUsuario')   
            # ----------------------------
              

        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña incorrectos...")
            return redirect('sesion:loginFormulario')
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('sesion:loginFormulario')
    else:
        messages.warning(request, "Usted no ha enviado datos...")
        return redirect('sesion:loginFormulario')

def logout(request):
    """
    Valida que la sesion del usuario este abierta y 
    realiza el borrado de la sesion
    """
    try:
        del request.session["logueo"]
        return redirect('landing')
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect('landing')