from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accion', views.accion, name = 'accion'),
     path('', views.peliculas_ranking, name='ranking'),
]