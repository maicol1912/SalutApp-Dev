from django.shortcuts import render, redirect
from database.models import Especificacion
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def listar(request):
    """
    Lista todos los registros almacenados de :model:`database.Especificacion`.
    en el template

    *return*
    si la cookie es admin redirecciona :template:`database/especificacion/listarEspecificacion.html`
    si la cookie no es admin retorna la ruta admin
    
    """
    if request.session["logueo"][1] =="admin":
        especificacion = Especificacion.objects.all()
        paginator = Paginator(especificacion, 5)
        page_number = request.GET.get('page')
        especificacion = paginator.get_page(page_number)

        context = {"datos": especificacion}
        return render(request, 'database/especificacion/listarEspecificacion.html', context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def formulario(request):
    """
    Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Especificacion`.

    **Template:**

    :template:`database/especificacion/registrarEspecificacion.html`
    """
    if request.session["logueo"][1] =="admin":
        return render(request, 'database/especificacion/registrarEspecificacion.html')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def ingresar(request):
    """
    Valida los datos entemplateviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Especificacion`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido
    """
    if request.session["logueo"][1] =="admin":
        try:
            if request.method == "POST":
                especificacion = Especificacion(especificacion_id = request.POST["especificacion_id"],
                                                especificacion_nombre = request.POST["especificacion_nombre"],
                                                especificacion_dia_1=request.POST["especificacion_dia_1"],
                                                especificacion_dia_2=request.POST["especificacion_dia_1"],
                                                especificacion_dia_3=request.POST["especificacion_dia_1"],
                                                especificacion_dia_4=request.POST["especificacion_dia_1"],
                                                especificacion_dia_5=request.POST["especificacion_dia_1"],
                                                especificacion_dia_6=request.POST["especificacion_dia_1"],
                                                especificacion_dia_7=request.POST["especificacion_dia_1"],
                            )
                especificacion.save()
                messages.success(request, "Especificacion guardada Correctamente")
            else:
                messages.warning(request, "usted no ha enviado datos...")

        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect('especificacion:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def eliminar(request, id):
    """
    Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.Encuesta`.
    """
    if request.session["logueo"][1] =="admin":
        especificacion = Especificacion.objects.get(pk=id)
        especificacion.delete()
        return redirect('especificacion:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def encontrar(request, id):
    """
    Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Especificacion`.

    **Template:**

    :template:`database/especificacion/actualizarEspecificacion.html`
    """
    if request.session["logueo"][1] =="admin":
        especificacion = Especificacion.objects.get(pk=id)
        context = {"datos": especificacion}
        return render(request, "database/especificacion/actualizarEspecificacion.html", context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def actualizar(request):
    """
    Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Especificacion`. si todo esta correcto
    """
    if request.session["logueo"][1] =="admin":
        id = request.POST["id"]

        especificacion = Especificacion.objects.get(pk=id)
        especificacion.especificacion_id = id 
        especificacion.especificacion_nombre = request.POST["especificacion_nombre"]
        especificacion.especificacion_dia_1 = request.POST["especificacion_dia_1"]
        especificacion.especificacion_dia_2 = request.POST["especificacion_dia_2"]
        especificacion.especificacion_dia_3 = request.POST["especificacion_dia_3"]
        especificacion.especificacion_dia_4 = request.POST["especificacion_dia_4"]
        especificacion.especificacion_dia_5 = request.POST["especificacion_dia_5"]
        especificacion.especificacion_dia_6 = request.POST["especificacion_dia_6"]
        especificacion.especificacion_dia_7 = request.POST["especificacion_dia_7"]
        especificacion.save()
        return redirect('especificacion:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def buscar(request):
    """
    Filtra el registro que se quiere encontrar de :model:`database.Especificacion`. 
    y se muestra sus datos en un template

    **Template:**

    :template:`database/especificacion/listarEspecificacion.html`
    """
    if request.session["logueo"][1] =="admin":
        from django.db.models import Q
        
        if request.method == "POST":
            dato = request.POST["buscar"]
            q = Especificacion.objects.filter(especificacion_nombre__contains = dato)
            
            paginator = Paginator(q, 5) # Mostrar 3 registros por página...

            page_number = request.GET.get('page')
            #Sobreescribir la salida de la consulta.......
            q = paginator.get_page(page_number)
            
            contexto = { "datos": q }
            return render(request, 'database/especificacion/listarEspecificacion.html', contexto)
        else:
            messages.error(request, "Error no envió datos...")
            return redirect('especificacion:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")