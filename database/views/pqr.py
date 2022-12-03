from django.shortcuts import render, redirect
from database.models import Pqr,Usuario
from django.contrib import messages
from django.core.paginator import Paginator



# Create your views here.
def listar(request):
    """Lista todos los registros almacenados de :model:`database.Pqr`.
    en el template

    Args:
        q: ninguno

    Returns:
       template:`database/pqr/listarPqr.html`
    """
    if request.session["logueo"][1] =="admin":
        pqr = Pqr.objects.all()
        paginator = Paginator(pqr, 5)
        page_number = request.GET.get('page')
        pqr = paginator.get_page(page_number)

        context = {"datos": pqr}
        return render(request, 'database/pqr/listarPqr.html', context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def formulario(request):
    """Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Pqr`.

    Args:
        q: ninguno

    Returns:
       template:`database/pqr/registrarPqr.html`
    """
    if request.session["logueo"][1] =="admin":
        usuario = Usuario.objects.all()
        context = {"usuarios":usuario}
        return render(request, 'database/pqr/registrarPqr.html',context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Pqr`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido

    Args:
        q: ninguno

    Returns:
       nada
    """
    
    if request.session["logueo"][1] =="admin":
        try:
            if request.method == "POST":
                usuarioP = request.POST["pqr_usuario"]
                usuario = Usuario.objects.get(pk=usuarioP)
                pqr = Pqr(pqr_tipo = request.POST["pqr_tipo"],
                        pqr_desc = request.POST["pqr_desc"],
                        usuario_id = usuario
                        )
                pqr.save()
                messages.success(request, "Pqr guardado Correctamente")
            else:
                messages.warning(request, "usted no ha enviado datos...")

        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect('pqr:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def eliminar(request, id):
    """Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.Pqr`.

    Args:
        q: recibe el id del pqr para poder eliminarlo

    Returns:
       nada
    """
    if request.session["logueo"][1] =="admin":
        pqr = Pqr.objects.get(pk=id)
        pqr.delete()
        return redirect('pqr:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def encontrar(request, id):
    """Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Pqr`.

    Args:
        q: recibe el id del pqr para poder renderizarlo

    Returns:
       template:`database/pqr/actualizarPqr.html`
    """
    
    if request.session["logueo"][1] =="admin":
        pqr = Pqr.objects.get(pk=id)
        usuario = Usuario.objects.all()
        context = {"datos": pqr,
                "usuarios":usuario}
        return render(request, "database/pqr/actualizarPqr.html", context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def actualizar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Pqr`. si todo esta correcto

    Args:
        q: ninguno

    Returns:
       nada
    """
    if request.session["logueo"][1] =="admin":
        usuarioP = request.POST["pqr_usuario"]
        usuario = Usuario.objects.get(pk=usuarioP)
        id = request.POST["id"]

        pqr = Pqr.objects.get(pk=id)
        pqr.id = id
        pqr.pqr_tipo = request.POST["encuesta_tipo"]
        pqr.pqr_desc = request.POST["encuesta_desc"]
        pqr.usuario_id = usuario
        pqr.save()
        return redirect('pqr:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def buscar(request):
    """Filtra el registro que se quiere encontrar de :model:`database.Pqr`. 
    y se muestra sus datos en un template

    Args:
        q: ninguno

    Returns:
       template:`database/pqr/listarPqr.html`
    """
    
    if request.session["logueo"][1] =="admin":
        from django.db.models import Q
        
        if request.method == "POST":
            dato = request.POST["buscar"]
            q = Pqr.objects.filter(pqr_tipo__contains = dato)
            
            paginator = Paginator(q, 5) # Mostrar 3 registros por página...

            page_number = request.GET.get('page')
            #Sobreescribir la salida de la consulta.......
            q = paginator.get_page(page_number)
            
            contexto = { "datos": q }
            return render(request, 'database/pqr/listarPqr.html', contexto)
        else:
            messages.error(request, "Error no envió datos...")
            return redirect('pqr:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")