from django.contrib import admin
from django.urls import path
from .views import *
from aplicacion import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include




urlpatterns = [
	path('nosotros/', AboutUs.as_view(), name='nosotros'),    
    path('proyectoAnual/<int:id>', ProgramaAnual.as_view(), name='proyectoAnual'),
    path('proyecto/<int:id>', Programa.as_view(), name='proyecto'),
    path('recursos/', Resources.as_view(), name = 'recurso'),
    path('colaboradores/', Partners.as_view(), name = 'colaborador'),

    path('noticias/', Prensa.as_view(), name = 'noticia'),
    path('infonoticia/<int:pk>', InfoPrensa.as_view(), name= 'infonoticia'),

    path('contacto/', Contacto.as_view(), name='contacto'),
 
  ]

    
admin.site.site_header = "Red Joven y Empleo"
admin.site.site_title = "Admin Red Joven y Empleo"
admin.site.index_title = "Bienvenido al Portal de la Red Joven y Empleo"
