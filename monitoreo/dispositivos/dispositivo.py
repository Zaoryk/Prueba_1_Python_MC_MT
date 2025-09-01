from django.db import models
from .categoria import Categoria
from .zona import Zona

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    consumo_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="dispositivos")
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="dispositivos")

    def __str__(self):
        return self.nombre