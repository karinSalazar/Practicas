from django.contrib import admin
from django.urls import path
from .views import *
from aplicacion import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include




urlpatterns = [
	path('nosotros/', AboutUs.as_view(), name='nosotros'),
    path('proyectos/<int:id>', Programa.as_view(), name='proyecto'),
    path('recursos/', Resources.as_view(), name = 'recurso'),
    path('colaboradores/', Partners.as_view(), name = 'colaborador'),     
    path('noticias/', Prensa.as_view(), name = 'noticia'),
    path('contacto/', Contacto.as_view(), name='contacto'),
 
  ]


    

  