from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hola mundo!')

#Importa módulo de biblioteca de python fechas y hora
import datetime

# Función hora actual almacena en variable now
# La segunda línea construye la respuesta html
# %s es yb narcadir de posición
# y al final de cadena reemplaza por valor now

def hora_actual(request):
    now = datetime.datetime.now()
    html = '<html><body><strong>¡Hola mundo!</strong><br>Fecha y Hora:%s.</body></html>'% now
    return HttpResponse(html)
