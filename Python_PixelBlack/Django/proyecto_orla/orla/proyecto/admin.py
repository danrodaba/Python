from django.contrib import admin
from .models import Curso, Orla

# Register your models here.

'''
Aquí creamos una nueva clase que va a heredar las clases Proyecto y Orla para hacer las modificaciones
en los models que trabajamos en el pad. Una vez creadas, le pedimos que muestre las clases Orla y Proyecto con 'list_display'.
Es interesante un campo de búsqueda para poder seleccionar registros filtrados con "select where".
Añado un filtro para poder filtrar en OrlaAdmin, los profesores y los alumnos y otro en Curso para poder 
filtrar los cursos por fecha.
Si trabajamos con fechas, podemos introducir un filtro de tipo menú horizontal que nos va indicando lo que filtramos.
'''
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo','subtitulo','fecha','logo')    #aquí falta 'num'
    search_display = ('num','titulo','fecha')
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'

class OrlaAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'nombre', 'apellidos', 'image', 'video', 'created', 'estado') #aquí falta "texto"
    search_field = ('propietario', 'nombre', 'numero')
    list_filter = ('estado',)


admin.site.register(Curso, CursoAdmin)
admin.site.register(Orla, OrlaAdmin)