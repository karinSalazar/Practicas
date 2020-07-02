from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.models import User
from .forms import ContactoForm
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from random import shuffle
from .forms import VideoForm

from django.db.models import Q




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
        send_mail(subject, message, contact_email, ['karen_t195@hotmail.com'], fail_silently = False)
        return super(Inicio, self).form_valid(form)

   
    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['nos'] = Nosotros.objects.all()
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        context['prensa'] = Noticia.objects.all()
        context['numero'] = Impacto.objects.all()
        context['enti'] = Entidad.objects.all()
        context['testi'] = Testimonio.objects.all().order_by('-id')[:5]
        listaVideos=Video.objects.all()
        if (len(listaVideos)>0): #Si hay videos
            lastvideo= Video.objects.all()[0]
            context['videofile']= lastvideo.videofile
            
        return context





class AboutUs(TemplateView):
    model = Nosotros
    template_name = 'aplicacion/nosotros.html'   
    context_object_name = 'nos'
    queryset = Nosotros.objects.all() 

   
    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        return context



    
class ProgramaAnual(ListView):
    model = ProyectoAnual
    template_name = 'aplicacion/proyectoAnual.html'
    context_object_name = 'anual'
    queryset = ProyectoAnual.objects.all()
                    
    def get_context_data(self, **kwargs):
        context=super(ProgramaAnual, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None)
        context['anualId']=ProyectoAnual.objects.filter(id=parametro)
        context['project'] = Proyecto.objects.all()
        listaVideos=Video.objects.all()
        if (len(listaVideos)>0): #Si hay videos
            lastvideo= Video.objects.all()[0]
            context['videofile']= lastvideo.videofile

        return context



class Programa(ListView):
    model = Proyecto
    template_name = 'aplicacion/proyecto.html'
    context_object_name = 'project'
    queryset = Proyecto.objects.all()
                    
    def get_context_data(self, **kwargs):
        context=super(Programa, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None)
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

    
    def year_archive(request, nombreRecurso):
        a_list = Recurso.objects.filter(pub_date__year=nombreRecurso)
        context = {'year': nombreRecurso, 'article_list': a_list}
        return render(request, 'aplicacion/recursos.html', context)


    def busqueda(self):
        q = request.GET.get('q', '')
        querys = (Q(proyecto__nombreProyecto__icontains=q) | Q(proyecto__nombreProyecto__icontains=q))
        querys |= Q(nombreRecurso__icontains=q)
        recursos = Recurso.objects.filter(querys)
        return render(request, 'aplicacion/recursos.html', {'res': recursos})
    
    """def Buscar(request):
                                if request.GET["dow"]:
                                    nombreRecurso = request.GET["dow"]
                                    articulo = Recurso.objects.filter(nombre_icontains=nombreRecurso)
                                    return render(request, "aplicacion/recursos.html",{"articulo": articulo, "query":nombreRecurso})
                                else: 
                                    mensaje = "No has introducido nada"
                                return HttpResponse(mensaje)
            """
    def get_context_data(self, **kwargs):
        context = super(Resources, self).get_context_data(**kwargs)
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
        send_mail(subject, message, contact_email, ['karen_t195@hotmail.com'], fail_silently = False)
        return super(Contacto, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Contacto, self).get_context_data(**kwargs)
        context['anual'] = ProyectoAnual.objects.all()
        context['project'] = Proyecto.objects.all()
        return context
       



     
    
