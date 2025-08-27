from django.db import models

from .categoria import Categoria
from .zona import Zona
from .dispositivo import Dispositivo
from .medicion import Medicion
from .alerta import Alerta

class BaseModel(models.Model):
    ESTADOS = [
        ("ACTIVO","Activo"),("INACTIVO","Inactivo"),
    ]
    estado = models.CharField(max_length=10,choices = ESTADOS, default = "ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True