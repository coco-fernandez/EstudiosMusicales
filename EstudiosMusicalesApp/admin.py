from django.contrib import admin

from EstudiosMusicalesApp.models import *
from .models import *

# Register your models here.

class EstudioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'ubicacion', 'cantidad_salas')
    search_fields = ('nombre', 'ubicacion', 'cantidad_salas')


class BandaAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'genero', 'cantidad_integrantes')
    search_fields = ('nombre', 'genero', 'cantidad_integrantes')


class ProductorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')
    # readonly_fields=("profesion",)


admin.site.register(Estudio,EstudioAdmin)
admin.site.register(Banda,BandaAdmin)
admin.site.register(Productor,ProductorAdmin)

# admin, admin -> python manage.py createsuperuser