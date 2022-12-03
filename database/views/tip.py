from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Tip
from django.core.paginator import Paginator

# Create your views here.


def listar(request):
    """Lista todos los registros almacenados de :model:`database.Tip`.
    en el template

    Args:
        q: ninguno

    Returns:
       template:`database/tip/listarTip.html`
    """
    if request.session["logueo"][1] =="admin":
        tip = Tip.objects.all()
        paginator = Paginator(tip,5)
        page_number = request.GET.get('page')
        tip = paginator.get_page(page_number)

        context = {"datos": tip}
        return render(request, 'database/tip/listarTip.html', context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")


def formulario(request):
    """Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Tip`.

    Args:
        q: ninguno

    Returns:
       template:`database/tip/registrarTip.html`
    """
    if request.session["logueo"][1] =="admin":
        return render(request, 'database/tip/registrarTip.html')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Tip`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido

    Args:
        q: ninguno

    Returns:
       nada
    """
    if request.session["logueo"][1] =="admin":
        try:
            if request.method == "POST":
                tip = Tip(tip_encabezado = request.POST["tip_encabezado"],
                               tip_desc = request.POST["tip_desc"])
                tip.save()
                messages.success(request, "Tip guardado Correctamente")
            else:
                messages.warning(request, "usted no ha enviado datos...")

        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect('tip:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def eliminar(request, id):
    """Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.Tip`.

    Args:
        q: recibe el id del tip para poder eliminarlo

    Returns:
       nada
    """
    if request.session["logueo"][1] =="admin":
        tip = Tip.objects.get(pk=id)
        tip.delete()
        return redirect('tip:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def encontrar(request, id):
    """Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Tip`.

    Args:
        q: recibe el id del tip para poder renderizarlo

    Returns:
       template:`database/tip/actualizarTip.html`
    """
    if request.session["logueo"][1] =="admin":
        tip = Tip.objects.get(pk=id)
        context = {"datos": tip}
        return render(request, "database/tip/actualizarTip.html",context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def actualizar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Tip`. si todo esta correcto

    Args:
        q: ninguno

    Returns:
       nada
    """
    
    if request.session["logueo"][1] =="admin":
        id = request.POST["id"]
        tip = Tip.objects.get(pk=id)

        tip.id = id
        tip.tip_encabezado = request.POST["tip_encabezado"]
        tip.tip_desc = request.POST["tip_desc"]
        tip.save()
        return redirect('tip:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def buscar(request):
    """Filtra el registro que se quiere encontrar de :model:`database.Tip`. 
    y se muestra sus datos en un template

    Args:
        q: ninguno

    Returns:
       template:`database/tip/listarTip.html`
    """
    if request.session["logueo"][1] =="admin":
        from django.db.models import Q
        
        if request.method == "POST":
            dato = request.POST["buscar"]
            q = Tip.objects.filter(tip_encabezado__contains = dato)
            
            paginator = Paginator(q, 5) # Mostrar 3 registros por página...

            page_number = request.GET.get('page')
            #Sobreescribir la salida de la consulta.......
            q = paginator.get_page(page_number)
            
            contexto = { "datos": q }
            return render(request, 'database/tip/listarTip.html', contexto)
        else:
            messages.error(request, "Error no envió datos...")
            return redirect('tip:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")