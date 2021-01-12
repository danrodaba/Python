from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render, get_object_or_404
from .models import Curso


def lista_proyecto(request): 
    return render(request, 'index.html', {'curso': Curso})
