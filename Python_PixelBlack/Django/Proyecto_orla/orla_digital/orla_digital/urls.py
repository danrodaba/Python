"""orla_digital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from orla import views

from django.conf import settings
from django.conf.urls.static import static
'''
Aqui vamos a relacionar los paths con el dominio. Eso quiere decir que el nombre definido aquí será lo que añadamos al dominio
para encontrar nuestra orla.
'''
urlpatterns = [
    path('', views.orla_list, name='orla_list'),
    path('homepage/', views.home, name='home'),     #aquí definimos que dominio/home será nuestra página de principal
    path('admin/', admin.site.urls),        #aquí definimos que dominio/admin será nuestra página de administración
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 