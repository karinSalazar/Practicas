from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from simple_history.models import HistoricalRecords


#from django.db.models import Count

# Create your models here.

class Colaborador(models.Model):
	nombreColaborador = models.CharField(max_length=40,verbose_name="Colaborador")
	link = models.URLField(max_length=500,null=True)
	logo = models.ImageField(upload_to ='Colaborador/',null=True)
		
	class Meta:
		verbose_name = 'Colaborador'
		verbose_name_plural = 'Colaboradores'

	def __str__(self):
		return str(self.nombreColaborador)



class Entidad(models.Model):
	nombreEntidad = models.CharField(max_length=40,null=True,verbose_name="Entidad")
	link = models.URLField(max_length=500,null=True)
	logo = models.ImageField(upload_to ='Entidades/',null=True)
	
	class Meta:
		verbose_name = 'Entidad'
		verbose_name_plural = 'Entidades'

	def __str__(self):
		return str(self.nombreEntidad)



class ProyectoAnual(models.Model):
	titulo = models.CharField(max_length=40,null=True,verbose_name="Título del Proyecto del Año")
	año = models.DateTimeField(auto_now_add=True, verbose_name="Año del Proyecto Anual")
	descripcion = models.TextField(max_length=800,null=True,verbose_name="Descripción")
	status =models.BooleanField(default=True,verbose_name="activo")
		
	class Meta:
		verbose_name = 'Proyecto_Anual'
		verbose_name_plural = 'Proyectos_Anuales'
		ordering = ['año']

	def __str__(self):
		return str(self.titulo)




class Proyecto(models.Model):
	nombreProyecto = models.CharField(max_length=40,null=True,verbose_name="Nombre del Proyecto")	
	año = models.DateTimeField(auto_now_add=True, verbose_name="Año del Proyecto")	
	proyectoAnual = models.ForeignKey(ProyectoAnual, on_delete=models.CASCADE,null=True,verbose_name="Proyecto Anual Vinculado")
	descripcion = models.CharField(max_length=300,null=True,verbose_name="Descripción")
	logros = models.CharField(max_length=300,null=True,verbose_name="Logros")
	imagen = models.ImageField(upload_to = 'imagesProyecto/',verbose_name="Imagen General")
	entidades = models.ForeignKey(Entidad, on_delete=models.CASCADE,null=True,verbose_name="Entidades Vinculado")
	videofile = models.FileField(upload_to='videoProyecto/', blank=True, verbose_name="Video del Proyecto Anual")
	history = HistoricalRecords()
	
	class Meta:
		verbose_name = 'Proyecto'
		verbose_name_plural = 'Proyectos'
		ordering = ['año']

	def __str__(self):
		return str(self.nombreProyecto)




class Imagen_Proyecto(models.Model):
	tituloProyecto = models.CharField(max_length=400,blank=True,null=True)	
	images = models.FileField(upload_to = 'imagesProyecto/')
	imagenes = models.ForeignKey(Proyecto, on_delete=models.CASCADE, blank=True,verbose_name="Imagenes Extras")
		
	class Meta:
		verbose_name = 'Imagen_Proyecto'
		verbose_name_plural = 'Imagenes_Proyectos'

	def __str__(self):
		return str(self.tituloProyecto)





class Noticia(models.Model):	
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
	fecha = models.DateField(blank=True, null=True, verbose_name="Fecha")
	creado_por = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Creado por")
	link = models.URLField(max_length=500, blank=True)
	titulo = models.CharField(max_length=100,blank=True, null=True,verbose_name="TÍtulo de la Noticia")
	descripcion = models.CharField(max_length=300,blank=True, null=True,verbose_name="Descripción de la Noticia")
	imagen = models.ImageField(upload_to = 'noticia/', default = 'noticia.jpg',verbose_name="Imagen")
	body = models.TextField(blank=True, null=True, verbose_name="Contenido de la Noticia")
	destacados = models.BooleanField(default=False)
    		
	class Meta:
		verbose_name = 'Noticia'
		verbose_name_plural = 'Noticias'
		ordering = ["-fecha"] 

	def __str__(self):
		return str(self.created) + " " + str(self.creado_por)+ " " + str(self.titulo)




class Recurso(models.Model):
	nombreRecurso = models.CharField(max_length=40, verbose_name="Nombre de la Transferencia")
	archivo = models.FileField(null=True,upload_to='transferencias/')
	link = models.URLField(null=True, blank=True)
	entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, null=True, verbose_name="Entidad vinculada")
	imagen = models.ImageField(upload_to ='recursos/', default = 'descarga.jpg')
	status =models.BooleanField(default=True, verbose_name="Si activa esta opción será público")

	class Meta:
		verbose_name = 'Recurso'
		verbose_name_plural = 'Recursos'

	def __str__(self):
		return str(self.nombreRecurso)



class Testimonio(models.Model):
	nombre = models.CharField(max_length=100,verbose_name="Nombre Completo")
	texto = models.CharField(max_length=300,verbose_name="Testimonio")
	foto = models.ImageField(upload_to = 'fotoTestimonio/',verbose_name="Foto")
	fecha = models.DateField(blank=True, null=True, verbose_name="Fecha")
	entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE,null=True,verbose_name="Entidad Vinculada")
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null=True,verbose_name="Proyecto Vinculado")
	
	
	class Meta:
		verbose_name = 'Testimonio'
		verbose_name_plural = 'Testimonios'

	def __str__(self):

		return str(self.nombre) + " " + str(self.fecha) + " " + str(self.entidad) + " " + str(self.proyecto)  



class Impacto(models.Model):
	nombre = models.CharField(max_length=40,verbose_name="Nombre Impacto Social")
	texto = models.CharField(max_length=150,verbose_name="Descripción")
	dato = models.IntegerField()

	class Meta:
		verbose_name = 'Impacto_Social'
		verbose_name_plural = 'Impacto_Social'

	def __str__(self):
		return str(self.nombre) + " " + str(self.dato)



class Nosotros(models.Model):
    titulo = models.CharField(max_length=250, null=True, verbose_name="Título")
    description = models.TextField(max_length=700, verbose_name="Descripción")
    imagen = models.ImageField(upload_to = 'nosotros/',verbose_name="Imagen")
    videofile= models.FileField(upload_to='nosotros/', null=True, verbose_name="Video")   
    direccion = models.CharField(max_length=80, null=True, blank=True, verbose_name="Dirección")
    tel = models.IntegerField(null= True,blank=True, verbose_name="Teléfono")
    mail = models.EmailField(null= True,blank=True, verbose_name="Correo")
    instagram = models.URLField(null=True,blank=True,verbose_name="Instagram")
    facebook= models.URLField(null=True,blank=True, verbose_name="Facebook")
    skype= models.URLField(null=True,blank=True, verbose_name="Skype")
    linkedin= models.URLField(null=True,blank=True, verbose_name="Linkedin")
    twitter= models.URLField(null=True,blank=True, verbose_name="Twitter")
    

    class Meta:
    	verbose_name = 'Nos'
    	verbose_name_plural = 'Nosotros'

    def __str__(self):
        return str(self.titulo)


