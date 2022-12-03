from django.shortcuts import render, redirect
from database.models import Plan, Especificacion,Usuario,Meta
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def listar(request):
    """Lista todos los registros almacenados de :model:`database.Plan`.
    en el template

    Args:
        q: ninguno

    Returns:
       template:`database/plan/listarPlan.html`
    """
    if request.session["logueo"][1] =="admin":
        plan = Plan.objects.all()
        paginator = Paginator(plan, 5)
        page_number = request.GET.get('page')
        plan = paginator.get_page(page_number)

        context = {"datos": plan}
        return render(request, 'database/plan/listarPlan.html', context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def formulario(request):
    """Renderiza un template el cual contiene los campos para ingresar
    los datos de :model:`database.Plan`.

    Args:
        q: ninguno

    Returns:
       template:`database/plan/registrarPlan.html`
    """
    if request.session["logueo"][1] =="admin":
        especificacion = Especificacion.objects.all()
        usuario = Usuario.objects.all()
        meta = Meta.objects.all()
        context = {"especificaciones": especificacion,"usuarios":usuario,"metas":meta}
        return render(request, 'database/plan/registrarPlan.html', context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def ingresar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la insercion a :model:`database.Plan`. si todo esta correcto
    o redirecciona nuevamente al mismo formulario hasta ser valido

    Args:
        q: ninguno

    Returns:
       nada
    """
    if request.session["logueo"][1] =="admin":
        try:
            if request.method == "POST":
                especificacionP = request.POST["plan_especificacion"]
                especificacion = Especificacion.objects.get(pk=especificacionP)
                metaP = request.POST["meta_especificacion"]
                meta = Meta.objects.get(pk=metaP)
                usuarioP = request.POST["usuario_especificacion"]
                usuario = Usuario.objects.get(pk=usuarioP)

                plan = Plan(plan_desc = request.POST["plan_desc"],
                            plan_recomendaciones = request.POST["plan_recomendacion"],
                            especificacion_id = especificacion,
                            meta_id = meta,
                            usuario_id = usuario
                            )
                plan.save()
                messages.success(request, "Plan guardada Correctamente")
            else:
                messages.warning(request, "usted no ha enviado datos...")

        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect('plan:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def eliminar(request, id):
    """Filtra el registro que se quiere eliminar, y hace el borrado del :model:`database.Plan`.

    Args:
        q: recibe el id del plan para poderlo eliminar

    Returns:
       nada
    """
    if request.session["logueo"][1] =="admin":
        plan = Plan.objects.get(pk=id)
        plan.delete()
        return redirect('plan:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def encontrar(request, id):
    """Filtra el registro que se quiere modificar y renderiza un formulario 
    para ingresar los campos del :model:`database.Plan`.

    Args:
        q: recibe el id del plan para renderizarlo

    Returns:
       template:`database/plan/actualizarPlan.html`
    """
    if request.session["logueo"][1] =="admin":
        plan = Plan.objects.get(pk=id)
        especificacion = Especificacion.objects.all()
        usuario = Usuario.objects.all()
        meta = Meta.objects.all()
        context = {"datos": plan,"especificaciones": especificacion,"usuarios":usuario,"metas":meta}
        return render(request, "database/plan/actualizarPlan.html", context)
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def actualizar(request):
    """Valida los datos enviados por el formulario, y asi poder
    hacer la actualizacion a :model:`database.Plan`. si todo esta correcto

    Args:
        q: ninguno

    Returns:
       nada
    """
    if request.session["logueo"][1] =="admin":
        especificacionP = request.POST["plan_especificacion"]
        especificacion = Especificacion.objects.get(pk=especificacionP)
        metaP = request.POST["meta_especificacion"]
        meta = Meta.objects.get(pk=metaP)
        usuarioP = request.POST["usuario_especificacion"]
        usuario = Usuario.objects.get(pk=usuarioP)
        id = request.POST["id"]

        plan = Plan.objects.get(pk=id)
        plan.id = id
        plan.plan_desc = request.POST["plan_desc"]
        plan.plan_recomendaciones = request.POST["plan_recomendacion"]
        plan.especificacion_id = especificacion
        plan.meta_id = meta
        plan.usuario_id = usuario
        plan.save()
        return redirect('plan:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")

def buscar(request):
    """Filtra el registro que se quiere encontrar de :model:`database.Plan`. 
    y se muestra sus datos en un template

    Args:
        q: ninguno

    Returns:
       template:`database/plan/listarPlan.html`
    """
    if request.session["logueo"][1] =="admin":
        from django.db.models import Q
        
        if request.method == "POST":
            dato = request.POST["buscar"]
            q = Plan.objects.filter(plan_desc__contains = dato)
            
            paginator = Paginator(q, 5) # Mostrar 3 registros por página...

            page_number = request.GET.get('page')
            #Sobreescribir la salida de la consulta.......
            q = paginator.get_page(page_number)
            
            contexto = { "datos": q }
            return render(request, 'database/plan/listarPlan.html', contexto)
        else:
            messages.error(request, "Error no envió datos...")
            return redirect('plan:listar')
    else:
        messages.warning(request, "usted no tiene acceso a este campo")
        return redirect("index")