from django.db import models
from .dispositivo import Dispositivo

class Medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="mediciones")
    fecha_hora = models.DateTimeField(auto_now_add=True)
    consumo_actual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.dispositivo.nombre} - {self.consumo_actual}W - {self.fecha_hora}"
