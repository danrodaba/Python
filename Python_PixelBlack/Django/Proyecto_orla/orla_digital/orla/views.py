from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Curso
from .models import Orla

'''
Llamamos orla y orla2 a los filtro para las bases de datos referentes a profesores y alumnos respectivamente.
Luego las devolvemos a la plantilla, en este caso "orla.html".

'''

def orla_list(request):
   curso = Curso.objects.filter(num='1')
   orla = Orla.objects.filter(estado='profe')
   orla2 = Orla.objects.filter(estado='alumno')
   return render(request, 'orla.html', {'curso': curso, 'orla': orla,'orla2': orla2})


# Falluto foerte. Ni caso.

def home(request):
    return HttpResponse('¡Hola Mundo!')

import io
from django.http import FileResponse
#from reportlab.pdfgen import canvas

'''
Aquí tratamos de poner la orla en pdf, pero es más duro que Chuck Norris veestido de Batman, así que finjamos que no existe.
'''

def some_view(request):
    # Creamos un buffer similar a un archivo, para recibir los datos del PDF
    buffer = io.BytesIO()

    # Creamos el objeto PDF, usando el buffer como su "archivo".
    p = canvas.Canvas(buffer)

    # Dibuja cosas en el PDF. Aquí es donde se genera el PDF.
    # Consulte la documentación de ReportLab para obtener la lista completa de funciones.
    p.drawString(100, 100, "Hello world.")

    # CCerramos el objeto PDF y listo
    p.showPage()
    p.save()

    # FileResponse establece el encabezado Content para los navegadores.
    # Presenta la opción de guardar el archivo.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='orla.pdf')