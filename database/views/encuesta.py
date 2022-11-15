from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Encuesta
from django.core.paginator import Paginator

# Create your views here.


def listar(request):
    """
    Lista todos los registros almacenados de :model:`database.Encuesta`.
    en el template

    **Template:**

    :template:`database/encuesta/listarEncuesta.html`
    """
    if request.session["logueo"][1] =="admin":
        encuesta = Encuesta.objects.all()
        paginator = Paginator(encuesta,5)
        page_number = request.GET.get('page')
        encuesta = paginator.get_page(page_number)

        context = {"datos": encuesta}
        return render(request, 'database/encuesta/listarEncuesta.html', context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")


def formulario(request):
    """
    Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Encuesta`.

    **Template:**

    :template:`database/encuesta/registrarEncuesta.html`
    """
    if request.session["logueo"][1] =="admin":
        return render(request, 'database/encuesta/registrarEncuesta.html')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def ingresar(request):
    """
    Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Encuesta`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido
    """
    if request.session["logueo"][1] =="admin":
        try:
            if request.method == "POST":
                encuesta = Encuesta(encuesta_tipo = request.POST["encuesta_tipo"],
                                    encuesta_desc = request.POST["encuesta_desc"],
                                    encuesta_estado=request.POST["encuesta_estado"])
                encuesta.save()
                messages.success(request, "Encuesta guardado Correctamente")
            else:
                messages.warning(request, "usted no ha enviado datos...")

        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect('encuesta:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def eliminar(request, id):
    """
    Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.Encuesta`.
    """
    if request.session["logueo"][1] =="admin":
        encuesta = Encuesta.objects.get(pk=id)
        encuesta.delete()
        return redirect('encuesta:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def encontrar(request, id):
    """
    Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Encuesta`.

    **Template:**

    :template:`database/encuesta/actualizarEncuesta.html`
    """
    if request.session["logueo"][1] =="admin":
        encuesta = Encuesta.objects.get(pk=id)
        context = {"datos": encuesta}
        return render(request, "database/encuesta/actualizarEncuesta.html",context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def actualizar(request):
    """
    Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Encuesta`. si todo esta correcto
    """
    if request.session["logueo"][1] =="admin":
        id = request.POST["id"]
        encuesta = Encuesta.objects.get(pk=id)
        encuesta.id = id
        encuesta.encuesta_tipo = request.POST["encuesta_tipo"]
        encuesta.encuesta_desc = request.POST["encuesta_desc"]
        encuesta.encuesta_estado = request.POST["encuesta_estado"]
        encuesta.save()
        return redirect('encuesta:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def buscar(request):
    """
    Filtra el registro que se quiere encontrar de :model:`database.Encuesta`. 
    y se muestra sus datos en un template

    **Template:**

    :template:`database/encuesta/listarEncuesta.html`
    """
    if request.session["logueo"][1] =="admin":
        from django.db.models import Q
        
        if request.method == "POST":
            dato = request.POST["buscar"]
            q = Encuesta.objects.filter(encuesta_tipo__contains = dato)
            
            paginator = Paginator(q, 5) # Mostrar 3 registros por página...

            page_number = request.GET.get('page')
            #Sobreescribir la salida de la consulta.......
            q = paginator.get_page(page_number)
            
            contexto = { "datos": q }
            return render(request, 'database/encuesta/listarEncuesta.html', contexto)
        else:
            messages.error(request, "Error no envió datos...")
            return redirect('encuesta:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")