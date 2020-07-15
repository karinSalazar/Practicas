from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.models import User
from .forms import ContactoForm, VideoNosForm, VideoProForm
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from random import shuffle







class Inicio(SuccessMessageMixin, FormView):
    form_class = ContactoForm
    template_name = 'index.html'
    success_url = reverse_lazy('inicio')
    success_message = "Tu mensaje ha sido enviado exitosamente. Gracias por contactarnos."
    

    def form_valid(self, form):
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        subject = form.cleaned_data['subject']
        message = "{0} tienes un nuevo mensaje:\n\n{1}".format(contact_name, form.cleaned_data['message'])
        send_mail(subject, message, contact_email, ['eve.redjoven@gmail.com'], fail_silently = False)
        return super(Inicio, self).form_valid(form)

   
    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['nos'] = Nosotros.objects.all()
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        context['prensa'] = Noticia.objects.all().order_by('-fecha')[:6]
        context['numero'] = Impacto.objects.all()
        context['enti'] = Entidad.objects.all()
        context['colaboradores'] = Colaborador.objects.all()
        context['testi'] = Testimonio.objects.all().order_by('-id')[:5]
        listaVideos=Nosotros.objects.all()
        if (len(listaVideos)>0): #Si hay videos
            lastvideo= Nosotros.objects.all()[0]
            context['videofile']= lastvideo.videofile
            
        return context





class AboutUs(TemplateView):
    model = Nosotros
    template_name = 'aplicacion/nosotros.html'   
    context_object_name = 'nos'
    queryset = Nosotros.objects.all() 

   
    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        context['numero'] = Impacto.objects.all()
        return context



    
class ProgramaAnual(ListView):
    model = ProyectoAnual
    template_name = 'aplicacion/proyectoAnual.html'
    context_object_name = 'anual'
    queryset = ProyectoAnual.objects.all()
                    
    def get_context_data(self, **kwargs):
        context=super(ProgramaAnual, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None)
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        context['anualId']=ProyectoAnual.objects.filter(id=parametro)
        context['project'] = Proyecto.objects.all()       
        return context



class Programa(ListView):
    model = Proyecto
    template_name = 'aplicacion/proyecto.html'
    context_object_name = 'project'
    queryset = Proyecto.objects.all()
                    
    def get_context_data(self, **kwargs):
        context=super(Programa, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None)
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        context['anual'] = ProyectoAnual.objects.all()
        context['pro']=Proyecto.objects.filter(id=parametro)
        context['ima']=Imagen_Proyecto.objects.all()
        return context




class Resources(ListView):
    paginate_by = 8
    model = Recurso
    template_name = 'aplicacion/recursos.html'
    context_object_name= 'res' 
    queryset = Recurso.objects.all()
    
    
    def get_context_data(self, **kwargs):
        context = super(Resources, self).get_context_data(**kwargs)
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        return context


    

class Partners(ListView):
    model = Colaborador
    template_name = 'aplicacion/colaboradores.html'

    def get_context_data(self, **kwargs):
        context = super(Partners, self).get_context_data(**kwargs)
        lista = list(Colaborador.objects.all())
        shuffle(lista)
        context['colaboradores'] = lista
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        return context




class Prensa(ListView):
    paginate_by = 4
    model = Noticia
    template_name = 'aplicacion/noticias.html'
    context_object_name = 'prensa'
    queryset = Noticia.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Prensa, self).get_context_data(**kwargs)
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        context['destacados']= Noticia.objects.filter(destacados = True)[:4]
        context['template']= 'aplicacion:noticia' 
        return context

      

class InfoPrensa(DetailView):
    template_name = 'aplicacion/infoNoticia.html'
    model =  Noticia

    def get_context_data(self, **kwargs):
        context = super(InfoPrensa, self).get_context_data(**kwargs)
        idnoticia = self.kwargs.get('pk',None)
        context['info'] = Noticia.objects.get(pk = idnoticia)
        context['template']= 'aplicacion:infonoticia'
        context['idTemp'] = idnoticia
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        return context

    
        

class Contacto(SuccessMessageMixin, FormView):
    form_class = ContactoForm
    success_url = reverse_lazy('aplicacion:contacto')
    template_name = 'aplicacion/contacto.html'
    success_message = "Tu mensaje fue enviado exitosamente. Gracias por contactarnos."
    
    def form_valid(self, form):
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        subject = form.cleaned_data['subject']
        message = "{0} tienes un nuevo mensaje:\n\n{1}".format(contact_name, form.cleaned_data['message'])
        send_mail(subject, message, contact_email, ['eve.redjoven@gmail.com'], fail_silently = False)
        return super(Contacto, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Contacto, self).get_context_data(**kwargs)
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        return context
       
       

class Privacidad(TemplateView):
    template_name = 'aplicacion/politicaPrivac.html'   

    def get_context_data(self, **kwargs):
        context = super(Privacidad, self).get_context_data(**kwargs)
        context['nos'] = Nosotros.objects.all()
        context['enti'] = Entidad.objects.all()
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        return context

 