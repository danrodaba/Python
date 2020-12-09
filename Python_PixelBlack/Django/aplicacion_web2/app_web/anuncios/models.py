from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Anuncio(models.Model): #clase tipo "base de datos"
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )

    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    image = models.ImageField(null=True, upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.titulo