from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import Tip
from django.contrib import messages


def listar(request):
    if request.session["logueo"][1] == "usuario" or request.session["logueo"][1] == "admin":
        
        tip = Tip.objects.all()
        context = {"datos": tip}
        return render(request, 'database/interfaces/interfazTip/listarTip.html', context)
        
    else:
        messages.warning(request, " No tienes acceso a este modulo")
        return redirect("indexUsuario")