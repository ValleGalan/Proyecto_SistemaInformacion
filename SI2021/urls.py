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
from SI2021.vista import plantilla_base,BaseLink
#from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import logout_then_login, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('registration/login/', LoginView.as_view(), name= 'login'),
    #path('logout/', LogoutView.as_view(), name= 'logout'),
    #path('accounts/LoginView/',LoginView,{'template_name':LoginView} , name="LoginView"),
    path('login/', LoginView.as_view(template_name='login.html')),#accounts/
    path('logout/', logout_then_login, name="logout"),
    
    path('plantilla_base/', plantilla_base),
    path('BaseLink/', BaseLink),
    path('baseAdmin/', vista.baseAdmin,name="baseAdmin"),
    
    path('index/', vista.index, name="index"),   
    path('inicio/', vista.inicio, name="inicio"),
    
    
    
     
    path('nosotros/', vista.nosotros, name="nosotros"),
    path('deportesExtremos/', vista.deportesExtremos, name="deportesExtremos"),
    path('disciplinasAlternativas/', vista.disciplinasAlternativas, name="disciplinasAlternativas"),
   
    path('contactar/', vista.contactar, name="contactar"),
    path('ubicacion/', vista.ubicacion, name="ubicacion"),
    path('perfil/', vista.perfil, name="perfil"),
    path('registro/', vista.registro, name="registro"),
    
    #--------------Funciones 
    path('lista_actividad/', vista.listActividad, name="lista_actividad"),
    
    path('agregar_profesional/', vista.agregar_profesional, name="agregar_profesional"),
    path('modificar_pro/<dni_profesional>/', vista.modificar_pro, name="modificar_pro"),
    path('eliminar_pro/<dni_profesional>/', vista.eliminar_pro, name="eliminar_pro"),
    path('agregar/', vista.agregar_actividad, name="agregar"),
    path('modificar/<cod_actividad>/', vista.modificar, name="modificar"),
    path('eliminar/<cod_actividad>/', vista.eliminar, name="eliminar"),

    #path('modificar/<pk>/', vista.post_edit, name="modificar"),
    path('ListaProfesional/', vista.listaAProfesional, name="ListaProfesional"),
    
    path('lista_profesional/', vista.listaProfesional,name="lista_profesional"),  
    path('yoga/', vista.listActividadYoga, name="yoga"),
    path('mensaje/', vista.mensaje, name="mensaje"),

    
    

]

