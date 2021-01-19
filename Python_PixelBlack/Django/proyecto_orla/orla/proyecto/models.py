from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Curso(models.Model):
    # creamos la clase
    titulo = models.CharField(max_length=150)
    subtitulo = models.TextField()
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(null='True', upload_to='images')

    def __str__(self):      #función que nos devuelve el título
        return self.num

class Orla(models.Model):   #ahora creamos la clase orla
    STATUS_CHOICES = (('profesor', 'Profesor'), ('alumno', 'Alumno'),)      #En este caso, vamos a tener dos estados.
    propietario = models.ForeignKey(Curso, on_delete=models.CASCADE)     #es una clave foranea. 
    nombre = models.TextField(max_length=100)
    apellidos = models.TextField(max_length=100)
    image = models.ImageField(null = True, upload_to='images')
    video = models.FileField(null = True, upload_to='videos')
    created = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices = STATUS_CHOICES, default = 'alumno')
    
    class Meta:  # Creamos la clase metadatos
        ordering = ('-apellidos',)  # Ordena por apellido

    def __str__(self):  # función que devuelve el titulo
        return self.titulo