
from django.contrib import admin
from django.urls import path

from dispositivos.views import inicio
from dispositivos.views import panel_dispositivos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('panel/', panel_dispositivos, name="panel"),
]
