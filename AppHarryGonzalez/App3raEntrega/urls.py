from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('libros', libros, name='Libros'),
    path('pelis', peliculas, name='Peliculas'),
    path('musica', musica, name='Musica'),
    path('agregar-libro', libro_formulario, name='AgregarLibros'),
    path('agregar-peli', peliculas_formulario, name='AgregarPeliculas'),
    path('agregar-musica', musica_formulario, name='AgregarMusica'),
    path('', inicio, name='Inicio'),
    path('busq-gen', busqueda_genero, name="BusquedaGenero"),
    path('buscar', buscar, name="Buscar"),
]