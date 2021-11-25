from django.db import models
from datetime import datetime
from django import forms
#---------------Para el administrador
'''
from django.contrib import admin
from DepNoConvencional.models import Author

class AuthorAdmin(admin.ModelAdmin):
    pass
class AuthorAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Author, AuthorAdmin)'''

    
#creo mis entidades las que voy a usar en la BD
#sqlite 3 , no es necesario instalarse algo ya q es nativo
class Usuario(models.Model):
    dni_usuario = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    TipoRol = (('admi','Administrador'),('user','Usuario'))
    rol =models.CharField(max_length=4,choices=TipoRol,default='user')
    email = models.EmailField(default='galan@gmail.com')
    contrasena = models.CharField(max_length=8) 
    #telefono = models.IntegerField()  
    #edad=models.IntegerField(default=20)
    #fechaRegistro = models.DateTimeField(default=datetime.now, blank=True)
    #indica que se va a guardar con la fecha en la que se guarda el registro   
    def nombreCompleto(self): #nombre completo del estudiante
	    txt ="{0} ,{1},{2}"
	    return txt.format(self.DNI_usuario,self.apellido,self.nombre)
    def __srt__(self): #contructor
        return self.nombreCompleto()
    
class Categoria(models.Model):
    id_categoria = models.CharField(max_length=3, primary_key=True)
    tipo_act = (('extremo','extremo'),('disciplina','disciplina'))
    tipo_actividad =models.CharField(max_length=12,choices=tipo_act,default='disciplina')
    clasificacion = models.CharField(max_length=40)
      
class Actividad(models.Model):
    cod_actividad = models.CharField(max_length=3, primary_key=True)
    descripcion = models.CharField(max_length=40)
    id_categoria = models.ForeignKey(Categoria, null=False,blank=False,on_delete=models.CASCADE)#foranea
 
class Profesional(models.Model):
    dni_profesional = models.CharField(max_length=8, primary_key=True) 
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    TipoRol = (('admi','Administrador'),('user','Usuario'))
    rol =models.CharField(max_length=4,choices=TipoRol,default='user')
    email = models.EmailField(default='valle@gmail.com')
    contrasena = models.CharField(max_length=8) 
    
    
class Lugar(models.Model):
    id_lugar = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=35)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10) 

class ActividadUsuario(models.Model): 
    dni_usuario = models.ForeignKey(Usuario, null=False,blank=False,on_delete=models.CASCADE)#foranea
    cod_actividad = models.ForeignKey(Actividad, null=False,blank=False,on_delete=models.CASCADE)

class ActividadProfesional(models.Model):
    dni_profesional = models.ForeignKey(Profesional, null=False,blank=False,on_delete=models.CASCADE)#foranea
    cod_actividad = models.ForeignKey(Actividad, null=False,blank=False,on_delete=models.CASCADE)

class ActividadLugar(models.Model):
    cod_actividad = models.ForeignKey(Profesional, null=False,blank=False,on_delete=models.CASCADE)#foranea
    id_lugar = models.ForeignKey(Lugar, null=False,blank=False,on_delete=models.CASCADE)
#DESPUES VOY A ADMIN.py PARA ADMINISTRAR MIS ENTIDADES
