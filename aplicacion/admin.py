from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *
from django.utils.html import format_html



#admin.site.register(Video)
admin.site.register(Colaborador)
admin.site.register(Entidad)
admin.site.register(Testimonio)
admin.site.register(Impacto)






@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ( "nombreRecurso", "descarga", "status")
    search_fields = ['nombreRecurso']
    list_per_page = 10 #paginar

    def descarga(self, obj):
        if obj.archivo:
            return format_html("<a class ='button button-skin text-center' href= '%s' download>Download</a>" % (obj.archivo.url,))
        else:
            return "No attachment"

    descarga.short_description = 'Ver Archivo'
    descarga.allow_tags = True







@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("created", "fecha", "titulo")
    search_fields = ['titulo']
    list_per_page = 10

    def order_count(self, obj):
        return obj._order_count

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'creado_por':
            kwargs['queryset'] = User.objects.filter(username=request.user.username)
        return super(NoticiaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('creado_por',)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['creado_por'] = request.user
        request.GET = data
        return super(NoticiaAdmin, self).add_view(request, form_url="", extra_context=extra_context)






class ProyectoImageAdmin(admin.StackedInline):
    model = Imagen_Proyecto
    

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto
    list_display = ("nombreProyecto", "año", "prueba2", "prueba",)
    search_fields = ['nombreProyecto']
    list_filter = [ 'proyectoAnual', 'entidades']
    history_list_display = ["nombreProyecto"]
    inlines = [ProyectoImageAdmin]
    list_per_page = 10

    class Meta:
       model = Proyecto

    def prueba(self, obj):
        return obj.proyectoAnual.titulo
    prueba.admin_order_field  = 'proyectoAnual'  
    prueba.short_description = 'Proyecto Anual' 


    def prueba2(self, obje):
        return obje.entidades
    prueba2.admin_order_field  = 'entidades'  
    prueba2.short_description = 'Entidades Vinculadas' 


@admin.register(Imagen_Proyecto)
class ProyectoImageAdmin(admin.ModelAdmin):
    pass



@admin.register(ProyectoAnual)
class ProyectoAnualAdmin(admin.ModelAdmin):
    model = ProyectoAnual
    list_display = ("titulo", "año", "status",)
    list_filter = [ 'status']
    history_list_display = ["titulo"]
    list_per_page = 10
   
 

    

class PostImageAdmin(admin.StackedInline):
    model = Imagen_Nosotros

@admin.register(Nosotros)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Nosotros

@admin.register(Imagen_Nosotros)
class PostImageAdmin(admin.ModelAdmin):
    pass

 