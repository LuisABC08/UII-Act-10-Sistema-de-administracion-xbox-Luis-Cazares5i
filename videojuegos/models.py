# videojuegos/models.py

from django.db import models

class Videojuego(models.Model):
    ID_Videojuego = models.AutoField(primary_key=True) # Clave primaria auto-incremental
    Titulo = models.CharField(max_length=200)
    Desarrollador = models.CharField(max_length=100)
    Genero = models.CharField(max_length=50)
    Plataforma = models.CharField(max_length=50)
    Fecha_Lanzamiento = models.DateField() # Campo para almacenar solo la fecha
    ID_Proveedor = models.IntegerField() # Campo para el ID del proveedor (puede ser una FK después)

    def __str__(self):
        # Representación legible de un objeto Videojuego
        return f"{self.Titulo} ({self.Plataforma})"

    class Meta:
        # Nombres más amigables en el panel de administración
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"