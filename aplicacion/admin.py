from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

admin.site.register(Video)
admin.site.register(Colaborador)
admin.site.register(Entidad)
admin.site.register(Recurso)



class PollHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "nombreProyecto", "año", "proyecto_del_año"]
    #history_list_display = ["proyecto_del_año"]
    history_list_display = ["status"]
    search_fields = ['nombreProyecto']
    
admin.site.register(Proyecto, PollHistoryAdmin)



class NoticiaAdmin(admin.ModelAdmin):
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

admin.site.register(Noticia, NoticiaAdmin)



"""class PostImageAdmin(admin.StackedInline):
    model = Imagen

@admin.register(Nosotros)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Nosotros

@admin.register(Imagen)
class PostImageAdmin(admin.ModelAdmin):
    pass"""