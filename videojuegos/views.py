# videojuegos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Videojuego
from .forms import VideojuegoForm

# Vista para mostrar la lista de todos los videojuegos
def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all() # Obtiene todos los objetos Videojuego de la base de datos
    return render(request, 'videojuegos/lista_videojuegos.html', {'videojuegos': videojuegos})

# Vista para añadir un nuevo videojuego
def añadir_videojuego(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa los datos del formulario
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el nuevo videojuego en la base de datos
            return redirect('lista_videojuegos') # Redirige a la lista de videojuegos
    else:
        # Si la solicitud es GET, muestra un formulario vacío
        form = VideojuegoForm()
    return render(request, 'videojuegos/añadir_videojuego.html', {'form': form})

# Vista para editar un videojuego existente
def editar_videojuego(request, pk): # 'pk' es la clave primaria del videojuego a editar
    videojuego = get_object_or_404(Videojuego, pk=pk) # Obtiene el videojuego o lanza un error 404
    if request.method == 'POST':
        # Si la solicitud es POST, actualiza el videojuego con los datos del formulario
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save() # Guarda los cambios
            return redirect('lista_videojuegos')
    else:
        # Si la solicitud es GET, muestra el formulario pre-llenado con los datos actuales del videojuego
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'videojuegos/editar_videojuego.html', {'form': form})

# Vista para eliminar un videojuego
def eliminar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)
    if request.method == 'POST':
        videojuego.delete() # Elimina el videojuego de la base de datos
        return redirect('lista_videojuegos')
    # Si la solicitud es GET, muestra una página de confirmación
    return render(request, 'videojuegos/confirmar_eliminacion.html', {'videojuego': videojuego})
def detalle_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk) # Obtiene el videojuego por su PK
    return render(request, 'videojuegos/detalle_videojuego.html', {'videojuego': videojuego})
