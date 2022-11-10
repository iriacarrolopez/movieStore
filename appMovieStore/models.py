from django.db import models

# Create your models here.

class Genero(models.Model):
	nombre = models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

class Director(models.Model):
	nombre = models.CharField(max_length=50)
	#fechaNac = models.DateField()
	#nacionalidad = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre

class Pelicula(models.Model):
	nombre = models.CharField(max_length=50)
	duracion = models.IntegerField(default=0)
	año = models.IntegerField(default=0)
	valoracion = models.IntegerField(default=0)
	#director = models.ForeignKey(Director, on_delete=models.CASCADE)
	#genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre