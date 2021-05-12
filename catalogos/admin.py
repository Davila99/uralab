from django.contrib import admin

from .models import Area, Sexo, Carrera, Laboratorio, Modalidad, Turno, Asignatura

class CarreraAdmin(admin.ModelAdmin):
    list_display=["carrera","area"]
    list_editable=["area"]
    search_fields=["carrera"]

admin.site.register(Area)
admin.site.register(Sexo)
admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Laboratorio)
admin.site.register(Modalidad)
admin.site.register(Turno)
admin.site.register(Asignatura)
# Register your models here.
