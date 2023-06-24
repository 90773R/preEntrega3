from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "inicio.html")

def libros(request):
    lista = Libro.objects.all()
    return render(request, "libros.html", {"libros": lista})

def peliculas(request):
    lista = Pelicula.objects.all()
    return render(request, "peliculas.html", {"peliculas": lista})

def musica(request):
    lista = Musica.objects.all()
    return render(request, "musica.html", {"musica": lista})

def libro_formulario(request):
    if request.method == 'POST':
        mi_formulario = Libro_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            libro = Libro(titulo=request.POST['titulo'], creador=request.POST['creador'], genero=request.POST['genero'], sinopsis=request.POST['sinopsis'])
            libro.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Libro_Formulario()
        return render(request, "libro_formulario.html", {"mi_formulario": mi_formulario})
    
def peliculas_formulario(request):
    if request.method == 'POST':
        mi_formulario = Peliculas_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            pelicula = Pelicula(titulo=request.POST['titulo'], creador=request.POST['creador'], genero=request.POST['genero'], sinopsis=request.POST['sinopsis'])
            pelicula.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Peliculas_Formulario()
        return render(request, "pelicula_formulario.html", {"mi_formulario": mi_formulario})
    
def musica_formulario(request):
    if request.method == 'POST':
        mi_formulario = Musica_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            musica = Musica(titulo=request.POST['titulo'], creador=request.POST['creador'], genero=request.POST['genero'])
            musica.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Musica_Formulario()
        return render(request, "musica_formulario.html", {"mi_formulario": mi_formulario})

def busqueda_genero(request):
    return render(request, "busqueda_genero.html")

def buscar(request):
    if request.GET["genero"]:
        genero = request.GET["genero"]
        peliculas = Pelicula.objects.filter(genero=genero)
        return render(request, "resultados_busqueda.html", {"peliculas": peliculas, "genero": genero})
    else:
        return HttpResponse("No enviaste info, por favor ingresa algo nuevamente")