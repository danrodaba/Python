from django.contrib import admin

# Register your models here.
from .models import Curso
admin.site.register(Curso)
from .models import Orla
admin.site.register(Orla)
