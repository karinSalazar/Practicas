from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *
from django.utils.html import format_html

from django.db.models import Count
from django.contrib.admin import ModelAdmin, register



@register(Colaborador)
class MaterialInfoAdmin(admin.ModelAdmin):
    icon_name = 'group_add'
    list_display = ( "nombreColaborador","hipervínculo",) #"logo",
    search_fields = ['nombreColaborador']
    list_per_page = 10 #paginar
    
    def hipervínculo(self, obj):
        return format_html( '<a target="_blank" href="{0}" >{0}</a>&nbsp;',obj.link)

    hipervínculo.short_description = 'Ver Vínculo'
    hipervínculo.allow_tags = True
    




@register(Entidad)
class MaterialTallerAdmin(admin.ModelAdmin):
    icon_name = 'account_balance'
    list_display = ( "nombreEntidad","hipervínculo",) #"logo",
    search_fields = ['nombreEntidad']
    list_per_page = 10 

    def hipervínculo(self, obj):
        return format_html( '<a target="_blank" href="{0}" >{0}</a>&nbsp;',obj.link)

    hipervínculo.short_description = 'Ver Vínculo'
    hipervínculo.allow_tags = True
    





@register(Impacto)
class MaterialCampaAdmin(admin.ModelAdmin):
    icon_name = 'public'
    list_display = ( "nombre","dato")
    list_per_page = 10 





@register(Nosotros)
class MaterialCampaAdmin(admin.ModelAdmin):
    icon_name = 'group'
    list_display = ( "titulo","tel","mail")





@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    icon_name = 'cast_connected'
    list_display = ("created", "fecha", "titulo", "creado_por", )
    search_fields = ['titulo']
    list_filter = ('created',)
    list_per_page = 10
    #exclude=("fecha ",)

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





@register(Testimonio)
class MaterialEventoAdmin(admin.ModelAdmin):
    icon_name = 'insert_comment'
    list_display = ( "nombre", "fecha", "entidad", "proyecto") #"foto",
    search_fields = ['nombre']
    list_filter = [ 'entidad','proyecto']
    list_per_page = 10 #paginar







@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    icon_name = 'unarchive'
    list_display = ( "nombreRecurso", "descarga", "status")
    search_fields = ['nombreRecurso']
    list_filter = [ 'status']
    list_per_page = 10 #paginar

    def descarga(self, obj):
        if obj.archivo:
            return format_html("<a class ='button button-skin text-center' href= '%s' download>Download</a>" % (obj.archivo.url,))
        else:
            return "No attachment"

    descarga.short_description = 'Ver Archivo'
    descarga.allow_tags = True






class ProyectoImageAdmin(admin.StackedInline):
    model = Imagen_Proyecto
    

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    icon_name = 'business_center'
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


"""@admin.register(Imagen_Proyecto)
class ProyectoImageAdmin(admin.ModelAdmin):
    pass"""



@admin.register(ProyectoAnual)
class ProyectoAnualAdmin(admin.ModelAdmin):
    icon_name = 'folder_special'
    model = ProyectoAnual
    list_display = ("titulo", "año", "status",)
    list_filter = [ 'status']
    search_fields = ['titulo']
    history_list_display = ["titulo"]
    list_per_page = 10
    #readonly_fields = ('status',)
   

    def get_readonly_display(self, request, obj=None):
           if obj:
               return ['status']
           else:
               return []
