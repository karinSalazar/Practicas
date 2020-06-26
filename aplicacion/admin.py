from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

from django.utils.html import format_html



admin.site.register(Video)
admin.site.register(Colaborador)
admin.site.register(Entidad)




@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ( "nombreRecurso", "custom_github_profile_url", "status")
    search_fields = ['nombreRecurso']


    def custom_github_profile_url(self, obj):
        return format_html(
        '<a  href="{0}" class="button">Archivo</a>&nbsp;',
        obj.archivo
        )

    custom_github_profile_url.short_description = 'Ver Archivo'
    custom_github_profile_url.allow_tags = True








@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("created", "fecha", "titulo")
    search_fields = ['titulo']


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





@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto
    list_display = ("nombreProyecto", "año", "prueba2", "prueba",)
    #search_fields = ['nombreProyecto']
    list_filter = [ 'proyectoAnual', 'entidades']
    history_list_display = ["nombreProyecto"]

    def prueba(self, obj):
        return obj.proyectoAnual.titulo
    prueba.admin_order_field  = 'proyectoAnual'  
    prueba.short_description = 'Proyecto Anual' 


    def prueba2(self, obje):
        return obje.entidades
    prueba2.admin_order_field  = 'entidades'  
    prueba2.short_description = 'Entidades Vinculadas' 





@admin.register(ProyectoAnual)
class ProyectoAnualAdmin(admin.ModelAdmin):
    model = ProyectoAnual
    list_display = ("titulo", "año", "status",)
    list_filter = [ 'status']
    history_list_display = ["titulo"]

   


"""class PostImageAdmin(admin.StackedInline):
    model = Proyecto
    list_display = ["id", "nombreProyecto", "año"]
    search_fields = ['nombreProyecto']

@admin.register(Proyecto)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Proyecto

@admin.register(Imagen_Proyecto)
class PostImageAdmin(admin.ModelAdmin):
    pass
"""




    

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

