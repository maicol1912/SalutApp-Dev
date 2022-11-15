from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Usuario
from django.contrib import messages
from django.core.paginator import Paginator
from database.views.encriptacion import encriptador


# Create your views here.


def listar(request):
    """
    Lista todos los registros almacenados de :model:`database.Usuario`.
    en el template

    **Template:**

    :template:`database/usuario/listarUsuario.html`
    """
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

def formulario(request):
    """
    Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Usuario`.

    **Template:**

    :template:`database/usuario/registrarUsuario.html`
    """
    if request.session["logueo"][1] =="admin":
        return render(request, 'database/usuario/registrarUsuarioAdmin.html')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

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

    return redirect('usuario:listar')


def eliminar(request, id):
    """
    Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.Usuario`.
    """
    if request.session["logueo"][1] =="admin":
        usuario = Usuario.objects.get(pk=id)
        usuario.delete()
        return redirect('usuario:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

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

def buscar(request):
    """
    Filtra el registro que se quiere encontrar de :model:`database.Usuario`. 
    y se muestra sus datos en un template

    **Template:**

    :template:`database/usuario/listarUsuario.html`
    """
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