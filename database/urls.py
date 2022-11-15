from django.urls import path, include
from .views import views

urlpatterns = [
    path('sesion/', include('database.url_modulos.sesion')),
    
    path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),
    path('index-usuario/', views.indexUsuario, name='indexUsuario'),
    
    path('sesion/', include('database.url_modulos.sesion')),

    path('encuesta/', include('database.url_modulos.encuesta')),
    path('especificacion/', include('database.url_modulos.especificacion')),
    path('meta/', include('database.url_modulos.meta')),
    path('plan/', include('database.url_modulos.plan')),
    path('pqr/', include('database.url_modulos.pqr')),
    path('tarea/', include('database.url_modulos.tarea')),
    path('usuario-encuesta/', include('database.url_modulos.usuario_encuesta')),
    path('usuario/', include('database.url_modulos.usuario')),
    path('i-usuario/', include('database.url_modulos.interfazUsuario')),
    path('i-meta/', include('database.url_modulos.interfazMeta')),
]
