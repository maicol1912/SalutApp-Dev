from django.shortcuts import render, redirect
from database.models import Usuario,Encuesta,UsuarioEncuesta
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.


def listar(request):
    """
    Lista todos los registros almacenados de :model:`database.UsuarioEncuesta`.
    en el template

    **Template:**

    :template:`database/usuario_encuesta/listarUsuarioEncuesta.html`
    """
    if request.session["logueo"][1] =="admin":
        usuarioEncuesta = UsuarioEncuesta.objects.all()
        paginator = Paginator(usuarioEncuesta, 5)
        page_number = request.GET.get('page')
        usuarioEncuesta = paginator.get_page(page_number)

        context = {"datos": usuarioEncuesta}
        return render(request, 'database/usuario_encuesta/listarUsuarioEncuesta.html', context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def formulario(request):
    """
    Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.UsuarioEncuesta`.

    **Template:**

    :template:`database/usuario_encuesta/registrarUsuarioEncuesta.html`
    """
    if request.session["logueo"][1] =="admin":
        usuario = Usuario.objects.all()
        encuesta = Encuesta.objects.all()
        context = {"usuarios": usuario,
                "encuestas":encuesta}
        return render(request, 'database/usuario_encuesta/registrarUsuarioEncuesta.html', context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def ingresar(request):
    """
    Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.UsuarioEncuesta`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido
    """
    if request.session["logueo"][1] =="admin":
        try:
            if request.method == "POST":
                usuarioP = request.POST["usuario_user"]
                usuario = Usuario.objects.get(pk=usuarioP)
                

                encuestaP = request.POST["usuario_enc"]
                encuesta = Encuesta.objects.get(pk=encuestaP)

                usuarioEncuesta = UsuarioEncuesta(usuario_id=usuario,
                                                encuesta_id=encuesta
                                                )
                usuarioEncuesta.save()
                messages.success(request, "Usuario Encuesta guardado Correctamente")
            else:
                messages.warning(request, "usted no ha enviado datos...")

        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect('usuarioEncuesta:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def eliminar(request, id):
    """
    Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.UsuarioEncuesta`.
    """
    if request.session["logueo"][1] =="admin":
        usuarioEncuesta = usuarioEncuesta.objects.get(pk=id)
        usuarioEncuesta.delete()
        return redirect('usuarioEncuesta:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def encontrar(request, id):
    """
    Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.UsuarioEncuesta`.

    **Template:**

    :template:`database/usuario_encuesta/actualizarUsuarioEncuesta.html`
    """
    if request.session["logueo"][1] =="admin":
        usuarioEncuesta = UsuarioEncuesta.objects.get(pk=id)
        usuario = Usuario.objects.all()
        encuesta = Encuesta.objects.all()
        context = {"datos": usuarioEncuesta,
                "usuarios": usuario,
                "encuestas":encuesta}
        return render(request, "database/usuario_encuesta/actualizarUsuarioEncuesta.html", context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def actualizar(request):
    """
    Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.UsuarioEncuesta`. si todo esta correcto
    """
    if request.session["logueo"][1] =="admin":
        usuarioP = request.POST["usuario_user"]
        usuario = Usuario.objects.get(pk=usuarioP)

        encuestaP = request.POST["usuario_enc"]
        encuesta = Usuario.objects.get(pk=encuestaP)

        id = request.POST["id"]

        usuarioEncuesta = UsuarioEncuesta.objects.get(pk=id)
        usuarioEncuesta.id = id
        usuarioEncuesta.usuario_id = usuario
        usuarioEncuesta.encuesta_id = encuesta
        
        usuarioEncuesta.save()
        return redirect('usuarioEncuesta:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def buscar(request):
    """
    Filtra el registro que se quiere encontrar de :model:`database.UsuarioEncuesta`. 
    y se muestra sus datos en un template

    **Template:**

    :template:`database/usuario_encuesta/listarUsuarioEncuesta.html`
    """
    if request.session["logueo"][1] =="admin":
        from django.db.models import Q
        
        if request.method == "POST":
            dato = request.POST["buscar"]
            q = UsuarioEncuesta.objects.filter(Q(usuario_id__contains = dato) | Q(encuesta_id__contains = dato))
            
            paginator = Paginator(q, 5) # Mostrar 3 registros por página...

            page_number = request.GET.get('page')
            #Sobreescribir la salida de la consulta.......
            q = paginator.get_page(page_number)
            
            contexto = { "datos": q }
            return render(request, 'database/usuario_encuesta/listarUsuarioEncuesta.html', contexto)
        else:
            messages.error(request, "Error no envió datos...")
            return redirect('usuarioEncuesta:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")