from django.db import models

class Alerta(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="alertas")
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tipo_alerta = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.tipo_alerta} - {self.dispositivo.nombre}"