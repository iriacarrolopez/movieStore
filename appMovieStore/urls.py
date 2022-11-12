from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listaDirectores', views.lista_directores, name = 'listaDirectores'),
    path('listaPeliculas', views.lista_peliculas, name = 'listaPeliculas'),
    path('listaGeneros', views.lista_generos, name = 'listaGeneros'),
    path('detailDirector/<int:director_id>', views.detail_director, name = 'detailDirector'),
    path('detailPelicula', views.detail_pelicula, name = 'detailPelicula'),
    path('detailGenero', views.detail_genero, name = 'detailGenero')
]