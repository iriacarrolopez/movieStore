from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pelicula, Genero, Director

def home(request):
	context = {}
	return render(request, "home.html", context)

#Devuelve un listado de directores
def lista_directores(request):
	lDirectores = Director.objects.all()
	context = {'lDirectores': lDirectores}
	return render(request, "listaDirectores.html", context)

def lista_peliculas(request):

	return render(request, "listaPeliculas.html", {})

def lista_generos(request):

	return render(request, "listaGeneros.html", {})

def detail_director(request, director_id):
	director = get_object_or_404(Director, pk=director_id)
	context = {'director': director}
	return render(request, "detailDirector.html", context)

def detail_pelicula(request):

	return render(request, "detailPelicula.html", {})	

def detail_genero(request):
	
	return render(request, "detailGenero.html", {})