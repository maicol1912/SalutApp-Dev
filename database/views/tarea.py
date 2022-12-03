from django.shortcuts import render, redirect
from database.models import Tarea,Especificacion,Usuario
from django.contrib import messages
from django.core.paginator import Paginator

def listar(request):
    """Lista todos los registros almacenados de :model:`database.Tarea`.
    en el template

    Args:
        q: ninguno

    Returns:
       template:`database/tarea/listarTarea.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            tarea = Tarea.objects.all()
            paginator = Paginator(tarea, 5)
            page_number = request.GET.get('page')
            tarea= paginator.get_page(page_number)

            context = {"datos": tarea}
            return render(request, 'database/tarea/listarTarea.html', context)
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def formulario(request):
    """Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Tarea`.

    Args:
        q: ninguno

    Returns:
       template:`database/tarea/registrarTarea.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            especificacion = Especificacion.objects.all()
            usuario = Usuario.objects.all()
            context = {"especificaciones": especificacion,
                    "usuarios":usuario}
            return render(request, 'database/tarea/registrarTarea.html', context)
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Tarea`. si todo esta correcto
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
                    especificacionP = request.POST["tarea_especificacion"]
                    especificacion = Especificacion.objects.get(pk=especificacionP)

                    if (request.POST["tarea_check"]=="falso"):
                        check = False
                    if (request.POST["tarea_check"] == "verdadero"):
                        check = True

                    usuarioP = request.POST["tarea_usuario"]
                    usuario = Usuario.objects.get(pk=usuarioP)

                    tarea = Tarea(  tarea_check = check,
                                    especificacion_id = especificacion,
                                    usuario_id = usuario
                                )
                    tarea.save()
                    messages.success(request, "Tarea guardada Correctamente")
                else:
                    messages.warning(request, "usted no ha enviado datos...")

            except Exception as e:
                messages.error(request, f"Error: {e}")

            return redirect('tarea:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def eliminar(request, id):
    """Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.Tarea`.

    Args:
        q: ninguno

    Returns:
       nada
    """
    try:
        if request.session["logueo"][1] =="admin":
            tarea = Tarea.objects.get(pk=id)
            tarea.delete()
            return redirect('tarea:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def encontrar(request, id):
    """Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Tarea`.

    Args:
        q: ninguno

    Returns:
       template:`database/tarea/actualizarTarea.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            tarea = Tarea.objects.get(pk=id)
            usuario = Usuario.objects.all()
            especificacion = Especificacion.objects.all()
            context = {"datos": tarea,
                    "usuarios": usuario,
                    "especificaciones":especificacion
                    }
            return render(request, "database/tarea/actualizarTarea.html", context)
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def actualizar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Tarea`. si todo esta correcto

    Args:
        q: ninguno

    Returns:
       nada
    """
    try:
        if request.session["logueo"][1] =="admin":
            usuarioP = request.POST["tarea_usuario"]
            usuario = Usuario.objects.get(pk=usuarioP)

            especificacionP = request.POST["tarea_especificacion"]
            especificacion = Especificacion.objects.get(pk=especificacionP)
            
            if (request.POST["tarea_check"] == "falso"):
                check = False
            if (request.POST["tarea_check"] == "verdadero"):
                check = True

            id = request.POST["id"]

            tarea = Tarea.objects.get(pk=id)
            tarea.id = id
            tarea.tarea_check = check
            tarea.especificacion_id = especificacion
            tarea.usuario_id = usuario
            tarea.save()
            return redirect('tarea:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")

def buscar(request):
    """Filtra el registro que se quiere encontrar de :model:`database.Tarea`. 
    y se muestra sus datos en un template

    Args:
        q: ninguno

    Returns:
       template:`database/tarea/listarTarea.html`
    """
    try:
        if request.session["logueo"][1] =="admin":
            from django.db.models import Q
            
            if request.method == "POST":
                dato = request.POST["buscar"]
                q = Tarea.objects.filter(usuario_id__contains = dato)
                
                paginator = Paginator(q, 5) # Mostrar 3 registros por página...

                page_number = request.GET.get('page')
                #Sobreescribir la salida de la consulta.......
                q = paginator.get_page(page_number)
                
                contexto = { "datos": q }
                return render(request, 'database/tarea/listarTarea.html', contexto)
            else:
                messages.error(request, "Error no envió datos...")
                return redirect('tarea:listar')
        else:
            messages.warning(request, "usted no tiene acceso a este campo")
            return redirect("index")
    except:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("index")




    

