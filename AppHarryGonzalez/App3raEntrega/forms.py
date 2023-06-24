from django import forms

class Libro_Formulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    creador = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)
    sinopsis = forms.CharField(max_length=200)

class Peliculas_Formulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    creador = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)
    sinopsis = forms.CharField(max_length=200)

class Musica_Formulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    creador = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)


