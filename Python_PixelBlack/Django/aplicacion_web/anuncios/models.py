from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Anuncio(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    estado = models.Charfield(max_length=10,
                            chices=STATUS_CHOICES,
                            default='draft')
    class Meta:     #creamos la clase metadatos
        ordering = ('-created',)
    def __str__(self):  #funcion que devuelve el título
        return self.titulo