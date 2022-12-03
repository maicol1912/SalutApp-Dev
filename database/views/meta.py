from tokenize import Number
from django.shortcuts import render, redirect
from database.models import Meta,Usuario
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def listar(request):
    """Lista todos los registros almacenados de :model:`database.Meta`.
    en el template

    Args:
        q: ninguno

    Returns:
       template:`database/meta/listarMeta.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            meta = Meta.objects.all()
            paginator = Paginator(meta, 5)
            page_number = request.GET.get('page')
            meta = paginator.get_page(page_number)

            context = {"datos": meta}
            return render(request, 'database/meta/listarMeta.html', context)
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def formulario(request):
    """Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Meta`.

    Args:
        q: ninguno

    Returns:
       template:`database/meta/registrarMeta.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            usuario = Usuario.objects.all()
            context = {"usuarios": usuario}
            return render(request, 'database/meta/registrarMeta.html', context)
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Meta`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido

    Args:
        q: ninguno

    Returns:
       nada
    """
    try:
        if request.session["logueo"][1] =="admin":
            try:
                if request.method == "POST":
                    usuarioP = request.POST["meta_usuario"]
                    usuario = Usuario.objects.get(pk=usuarioP)

                    meta = Meta(meta_tipo = request.POST["meta_tipo"],
                                meta_desc = request.POST["meta_desc"],
                                meta_peso_ideal = float(request.POST["meta_peso"]),
                                usuario_id = usuario
                            )
                    meta.save()
                    messages.success(request, "Meta guardada Correctamente")
                else:
                    messages.warning(request, "usted no ha enviado datos...")

            except Exception as e:
                messages.error(request, f"Error: {e}")

            return redirect('meta:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def eliminar(request, id):
    """Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.Meta`.

    Args:
        q: recibe el id del usuario para eliminarlo

    Returns:
       nada
    """
    try:
        if request.session["logueo"][1] =="admin":
            meta = Meta.objects.get(pk=id)
            meta.delete()
            return redirect('meta:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def encontrar(request, id):
    """Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Meta`.

    Args:
        q: recibe el id del usuario para renderizarlo

    Returns:
       template:`database/meta/actualizarMeta.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            meta = Meta.objects.get(pk=id)
            usuario = Usuario.objects.all()
            context = {"datos": meta,
                    "usuarios": usuario}
            return render(request, "database/meta/actualizarMeta.html", context)
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def actualizar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Meta`. si todo esta correcto

    Args:
        q: ninguno

    Returns:
       nada
    """
    try:
        if request.session["logueo"][1] =="admin":
            usuarioP = request.POST["meta_usuario"]
            usuario = Usuario.objects.get(pk=usuarioP)
            id = request.POST["id"]

            meta = Meta.objects.get(pk=id)
            meta.id = id
            meta.meta_tipo = request.POST["meta_tipo"]
            meta.meta_desc = request.POST["meta_desc"]
            meta.meta_peso_ideal = float(request.POST["meta_peso"])
            meta.usuario_id = usuario
            meta.save()
            return redirect('meta:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def buscar(request):
    """Filtra el registro que se quiere encontrar de :model:`database.Meta`. 
    y se muestra sus datos en un template

    Args:
        q: ninguno

    Returns:
       template:`database/meta/listarMeta.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            from django.db.models import Q
            
            if request.method == "POST":
                dato = request.POST["buscar"]
                q = Meta.objects.filter(meta_tipo__contains = dato)
                
                paginator = Paginator(q, 5) # Mostrar 3 registros por página...

                page_number = request.GET.get('page')
                #Sobreescribir la salida de la consulta.......
                q = paginator.get_page(page_number)
                
                contexto = { "datos": q }
                return render(request, 'database/meta/listarMeta.html', contexto)
            else:
                messages.error(request, "Error no envió datos...")
                return redirect('meta:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")





    

