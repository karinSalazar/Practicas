from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from simple_history.models import HistoricalRecords

from django.db.models import Count




# Create your models here.

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    class Meta:
    	verbose_name = 'Video'
    	verbose_name_plural = 'Videos'

    def __str__(self):
    	return str(self.name) + ": " + str(self.videofile)



class Colaborador(models.Model):
	nombreColaborador = models.CharField(max_length=40)
	link = models.URLField(max_length=500,null=True)
	logo = models.ImageField(upload_to ='Colaborador/',null=True)
	fecha = models.DateField(null=True)
	
	class Meta:
		verbose_name = 'Colaborador'
		verbose_name_plural = 'Colaboradores'

	def __str__(self):
		return str(self.nombreColaborador)


class Entidad(models.Model):
	nombreEntidad = models.CharField(max_length=40)
	link = models.URLField(max_length=500,null=True)
	logo = models.ImageField(upload_to ='Entidades/',null=True)
	
	
	class Meta:
		verbose_name = 'Entidad'
		verbose_name_plural = 'Entidades'

	def __str__(self):
		return str(self.nombreEntidad)





class Proyecto(models.Model):
	order = models.IntegerField(blank=True, null=True)
	nombreProyecto = models.CharField(max_length=40,null=True)
	año = models.DateTimeField('fecha')
	entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE,blank=True)
	descripcion = models.CharField(max_length=300,null=True)
	video = models.FileField(upload_to='proyecto/', null=True, verbose_name="video")
	history = HistoricalRecords()

	
	class Meta:
		verbose_name = 'Proyecto'
		verbose_name_plural = 'Proyectos'
		ordering = ['order']

	def __str__(self):
		return str(self.nombreProyecto)

class Imagen_Proyecto(models.Model):
	tituloProyecto = models.CharField(max_length=400,blank=True,null=True)	
	images = models.FileField(upload_to = 'images/')
	imagenes = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = 'Imagen_Proyecto'
		verbose_name_plural = 'Imagenes_Proyectos'

	def __str__(self):
		return str(self.tituloProyecto)


class Proyecto_del_año(models.Model):
	order = models.IntegerField(blank=True, null=True)
	titulo = models.CharField(max_length=40,null=True)
	año = models.DateTimeField('fecha')
	descripcion = models.CharField(max_length=300,null=True)
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,blank=True)
	proyecto_del_año =models.BooleanField(default=True,verbose_name='proyecto_del_año')
	

	
	class Meta:
		verbose_name = 'Proyecto_del_año'
		verbose_name_plural = 'Proyectos_del_año'
		ordering = ['order']

	def __str__(self):
		return str(self.titulo)


class Noticia(models.Model):
	order = models.IntegerField(blank=True, null=True)
	fecha = models.DateField(blank=True, null=True)
	creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
	link = models.URLField(max_length=500, blank=True)
	titulo = models.CharField(max_length=100,blank=True, null=True)
	descripcion = models.CharField(max_length=300,blank=True, null=True)
	imagen = models.FileField(upload_to = 'noticia/', default = 'noticia.jpg')
	body = models.TextField(blank=True, null=True)
		
	class Meta:
		verbose_name = 'Noticia'
		verbose_name_plural = 'Noticias'
		ordering = ["-fecha"] 

	def __str__(self):
		return str(self.order) + " " + str(self.creado_por)+ " " + str(self.fecha) + " " + str(self.titulo)




class Recurso(models.Model):
	nombreRecurso = models.CharField(max_length=40)
	archivo = models.FileField(null=True,upload_to='transferencias/')
	link = models.URLField(null=True, blank=True)
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
	imagen = models.ImageField(upload_to ='recursos/', default = 'descarga.jpg')
	status =models.BooleanField(default=True,verbose_name='status')


	class Meta:
		verbose_name = 'Recurso'
		verbose_name_plural = 'Recursos'

	def __str__(self):
		return str(self.nombreRecurso)




class Nosotros(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)

    class Meta:
    	verbose_name = 'Imagen'
    	verbose_name_plural = 'Imagenes'

    def __str__(self):
        return str(self.title)


class Imagen_Nosotros(models.Model):
	titulo = models.CharField(max_length=400,blank=True,null=True)
	images = models.FileField(upload_to = 'images/')
	imagenes = models.ForeignKey(Nosotros, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = 'Imagen_Nosotros'
		verbose_name_plural = 'Imagenes_Nosotros'

	def __str__(self):
		return str(self.titulo)




