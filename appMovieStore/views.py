from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pelicula, Genero, Director

# Create your views here.
def index(request):
	context = {}
	return render(request, "index.html", context)

def accion(request):
	return render(request, "accion.html", {})

#Devuelve los detalles de una películas
def detail_pelicula(request, pelicula_id):
	pelicula = get_object_or_404(Pelicula, pk=pelicula_id);
	context = {'pelicula': pelicula}
	return render(request, "", context)

# #Devuelve los detalles de un director
def detail_director(request, director_id):
	director = get_object_or_404(Director, pk=director_id);
	context = {'director': director}
	return render(request, '', context)

# #Devuelve las películas de un determinado género
def peliculas_genero(request, genero_id, pelicula_id):
	genero = get_object_or_404(Genero, pk=genero_id)
	pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
	peliculas = genero.pelicula_set.all()
	context = {'genero': genero, 'pelicula': pelicula}
	return render(request, '', context)


