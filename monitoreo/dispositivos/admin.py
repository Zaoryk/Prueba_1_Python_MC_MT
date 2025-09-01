from django.contrib import admin

from .models import Categoria, Zona, Dispositivo

admin.site.register([Categoria, Zona])

admin.site.register(Dispositivo)
