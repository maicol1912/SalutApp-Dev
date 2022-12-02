from django import views
from django.urls import path, include
from database.views import sesion

app_name = "sesion"

urlpatterns =[
    path('loginFormulario/', sesion.loginFormulario, name="loginFormulario" ),
    path('login/', sesion.login, name="login" ),
    path('logout/', sesion.logout, name="logout" )
]
