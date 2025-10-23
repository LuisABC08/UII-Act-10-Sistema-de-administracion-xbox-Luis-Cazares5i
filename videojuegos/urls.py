# videojuegos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_videojuegos, name='lista_videojuegos'),
    path('añadir/', views.añadir_videojuego, name='añadir_videojuego'),
    path('editar/<int:pk>/', views.editar_videojuego, name='editar_videojuego'),
    path('eliminar/<int:pk>/', views.eliminar_videojuego, name='eliminar_videojuego'),
    path('detalle/<int:pk>/', views.detalle_videojuego, name='detalle_videojuego'), # <--- ¡Nueva línea!
]
