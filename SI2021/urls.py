"""SI2021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from SI2021 import vista

from SI2021.vista import usuario

from SI2021.vista import plantilla_base
from SI2021.vista import ListaModificar
from SI2021.vista import BaseLink

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantilla_base/', plantilla_base),
    path('BaseLink/', BaseLink),
     path('index/', vista.index, name="index"),   
    path('inicio/', vista.inicio, name="inicio"),
    path('login/', vista.login, name="login"),
    path('nosotros/', vista.nosotros, name="nosotros"),
    path('deportesExtremos/', vista.deportesExtremos, name="deportesExtremos"),
    path('disciplinasAlternativas/', vista.disciplinasAlternativas, name="disciplinasAlternativas"),
    path('yoga/', vista.yoga, name="yoga"),
    path('perfil/', vista.perfil, name="perfil"),
    
    path('ListaModificar/', ListaModificar), 
    path('usuario/', usuario),

]

