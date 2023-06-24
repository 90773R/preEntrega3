from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    creador = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    sinopsis = models.TextField()
    def __str__(self):
        return f"{self.titulo} - {self.creador} - {self.genero}"

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    creador = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    sinopsis = models.TextField()
    def __str__(self):
        return f"{self.titulo} - {self.creador} - {self.genero}"

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    creador = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.titulo} - {self.creador} - {self.genero}"
