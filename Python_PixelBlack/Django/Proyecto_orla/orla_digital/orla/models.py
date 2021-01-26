# Importamos tablas, zona horaria y panel user
from django.db import models


'''
Creamos 2 tablas relacionadas entre sí con el modelo 1 a muchos.
Para ello creamos primero la clase Curso, que se relacionará con la clase orla.
En la primera almacenaremos los distintos cursos que hemos tenido, y lo relacionamos
con la orla, que contiene los profesores y alumnos del curso concreto.

En el caso de Orla, debemos diferenciar entre profesores y alumnos, generaremos una 
foreign key para relacionarla con la tabla curso.

'''
class Curso(models.Model):
       num = models.IntegerField(null=False, unique=True)
       titulo = models.CharField(max_length=150)
       subtitulo = models.CharField(max_length=150)
       Fecha = models.CharField(max_length=150)
       logo = models.ImageField(null=True, upload_to='images')

class Orla(models.Model):   #creamos la clase Orla
    STATUS_CHOICES = (         #definimos los estados
        ('profe', 'Profesor'),
        ('alumno', 'Alumno'),
    )
    owner = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    texto = models.TextField()
    image = models.ImageField(null=True, upload_to='images')
    video = models.FileField(null=True, upload_to='videos')
    created = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='alumno')
    class Meta:   #Creamos la clase metadatos
        ordering = ('apellidos',) #Ordena por fecha
    def __str__(self):  # función que devuelve el titulo
        return self.apellidos
