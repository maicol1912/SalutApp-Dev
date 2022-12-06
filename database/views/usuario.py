from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Usuario
from django.contrib import messages
from django.core.paginator import Paginator
from database.views.encriptacion import encriptador
from datetime import datetime


# Create your views here.


def listar(request):
    """Lista todos los registros almacenados de :model:`database.Usuario`.
    en el template

    Args:
        q: ninguno

    Returns:
       template:`database/usuario/listarUsuario.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            usuario = Usuario.objects.all()
            paginator = Paginator(usuario, 5)
            page_number = request.GET.get('page')
            usuario = paginator.get_page(page_number)

            context = {"datos": usuario}
            return render(request, 'database/usuario/listarUsuario.html', context)
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def formulario(request):
    """Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Usuario`.

    Args:
        q: ninguno

    Returns:
       template:`database/usuario/registrarUsuario.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            return render(request, 'database/usuario/registrarUsuarioAdmin.html')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Usuario`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido

    Args:
        q: ninguno

    Returns:
       nada
    """
    try:
        
        if request.method == "POST":
                altura = int(request.POST["usuario_altura"])
                peso = int(request.POST["usuario_peso"])
                edad = int(request.POST["usuario_edad"])
                user = request.POST["usuario_nombre"]
                password = request.POST["usuario_password"]
                if altura > 140 and peso > 40 and edad>=15 and len(password) >=6 and len(user)>=6:
                    correo = request.POST["usuario_correo"]
                    id = request.POST["usuario_id"]
                    if (Usuario.objects.filter(usuario_nombre=user) or Usuario.objects.filter(usuario_correo=correo) or Usuario.objects.filter(usuario_id=id)):
                        messages.warning(
                            request, "La informacion esta en uso")
                        return redirect("indexUsuario")
                    else:
                        passwordEncriptado = encriptador.encriptarPassword(password)
                        fechaIngreso = datetime.strftime(datetime.now(), "%d-%m-%Y")
                        usuario = Usuario(usuario_id=id,
                                          usuario_nombre=user,
                                          usuario_correo=correo,
                                          usuario_password=passwordEncriptado,
                                          usuario_peso=peso,
                                          usuario_altura=altura,
                                          usuario_edad=edad,
                                          usuario_rol=request.POST["usuario_rol"],
                                          usuario_nro_semanas= 0,
                                          usuario_fecha_avance=fechaIngreso,
                                          usuario_nro_tarea = 0
                                          )
                        usuario.save()
                        messages.success(
                            request, "Usuario guardado Correctamente")
                else:
                    messages.warning(
                        request, "Los datos que ingresaste no son validos")
        else:
            messages.warning(request, "usted no ha enviado datos...")

    except Exception as e:
        messages.error(request, f"Error: {e}")

    return redirect('usuario:listar')


def eliminar(request, id):
    """Filtra el registro que se quiere eliminar, y hace el borrado de usuarios del :model:`database.Usuario`.

    Args:
        q: recibe el id del usuario para poder eliminarlo

    Returns:
       nada
    """
    try:
        if request.session["logueo"][1] =="admin":
            usuario = Usuario.objects.get(pk=id)
            if usuario.usuario_rol == "admin":
                messages.warning(request, "usted no puede eliminar un admin")
                return redirect("index")
            else:
                usuario.delete()
                return redirect('usuario:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def encontrar(request, id):
    """Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Usuario`.

    Args:
        q: recibe el id del usuario para poder renderizarlo

    Returns:
       template:`database/usuario/actualizarUsuario.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            usuario = Usuario.objects.get(pk=id)
            context = {"datos": usuario}
            return render(request, "database/usuario/actualizarUsuario.html", context)
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def actualizar(request): 
    """Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Usuario`.

    Args:
        q: recibe el id del usuario para poder renderizarlo

    Returns:
       template:`database/usuario/actualizarUsuario.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            
            id = request.POST["usuario_id"]
            password = request.POST["usuario_password"]
            passwordEncriptado = encriptador.encriptarPassword(password)

            usuario = Usuario.objects.get(pk=id)
            usuario.usuario_id = id
            usuario.usuario_nombre = request.POST["usuario_nombre"]
            usuario.usuario_correo = request.POST["usuario_correo"]
            if len(password) >=6:
                usuario.usuario_password = passwordEncriptado
            else:
                usuario.usuario_password = usuario.usuario_password

            usuario.usuario_peso = int(request.POST["usuario_peso"])
            usuario.usuario_altura = int(request.POST["usuario_altura"])
            usuario.usuario_edad = int(request.POST["usuario_edad"])
            usuario.usuario_rol = request.POST["usuario_rol"]
            if usuario.usuario_altura > 140 and usuario.usuario_peso > 40 and usuario.usuario_edad>=15 and len(usuario.usuario_nombre)>=6:
                usuario.save()
            else:
                messages.warning(request, "Datos incorrectos")
                return redirect('usuario:listar')
            return redirect('usuario:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def buscar(request):
    """Filtra el registro que se quiere encontrar de :model:`database.Usuario`. 
    y se muestra sus datos en un template

    Args:
        q: ninguno

    Returns:
       template:`database/usuario/listarUsuario.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            from django.db.models import Q
            
            if request.method == "POST":
                dato = request.POST["buscar"]
                q = Usuario.objects.filter(Q(usuario_nombre__contains = dato) | Q(usuario_correo__contains = dato))
                
                paginator = Paginator(q, 5) # Mostrar 3 registros por página...

                page_number = request.GET.get('page')
                #Sobreescribir la salida de la consulta.......
                q = paginator.get_page(page_number)
                
                contexto = { "datos": q }
                return render(request, 'database/usuario/listarUsuario.html', contexto)
            else:
                messages.error(request, "Error no envió datos...")
                return redirect('usuario:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")





    

