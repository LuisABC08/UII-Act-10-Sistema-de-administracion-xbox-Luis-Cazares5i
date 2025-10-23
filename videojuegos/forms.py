# videojuegos/forms.py

from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        # Define qué campos de tu modelo quieres incluir en el formulario
        fields = ['Titulo', 'Desarrollador', 'Genero', 'Plataforma', 'Fecha_Lanzamiento', 'ID_Proveedor']
        # O puedes usar '__all__' para incluir todos los campos:
        # fields = '__all__'
        
        # Widgets para controlar cómo se renderizan los campos en HTML
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Desarrollador': forms.TextInput(attrs={'class': 'form-control'}),
            'Genero': forms.TextInput(attrs={'class': 'form-control'}),
            'Plataforma': forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha_Lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # Importante para un selector de fecha HTML5
            'ID_Proveedor': forms.NumberInput(attrs={'class': 'form-control'}),
        }