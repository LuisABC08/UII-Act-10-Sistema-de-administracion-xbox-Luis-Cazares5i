# videojuegos/admin.py

from django.contrib import admin
from .models import Videojuego # Importa tu modelo

admin.site.register(Videojuego) # Registra el modelo