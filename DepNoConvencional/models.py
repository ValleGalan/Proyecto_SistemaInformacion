from django.db import models
from datetime import datetime
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
    
'''f        
class Categoria(models.Model):
    id_categoria = models.CharField(max_length=3, primary_key=True)
    tipo_act = (('extremo','extremo'),('disciplina','disciplina'))
    tipo_actividad =models.CharField(max_length=12,choices=tipo_act,default='disciplina')
    clasificacion = models.CharField(max_length=40)  
'''
      
class Actividad(models.Model):
    cod_actividad = models.CharField(max_length=3, primary_key=True)
     
    tipo_act = (('yoga','yoga'),('golf','golf'),('tenis','tenis'),('tenis de mesa','tenis de mesa'),('padel','padel')
                ,('ejercicio al agua','ejercicio al agua'),('parkur','parkur'),('trekking','trekking')
                ,('rappel','rappel'),('roller skating','roller skating'),('montañismo','montañismo'))
    list_actividad =models.CharField(max_length=20,choices=tipo_act,default='disciplina') 
    localidad = (('Cochinoca','Cochinoca'),('Dr. Manuel Belgrano','Dr. Manuel Belgrano'),('El Carmen','El Carmen'),
               ('Humahuaca','Humahuaca'),('Ledesma','Ledesma'),('Palpalá','Palpalá'),('Rinconada','Rinconada'),('San Antonio','San Antonio')
                ,('San Pedro','San Pedro'),('Santa Bárbara','Santa Bárbara'),('Santa Catalina','Santa Catalina'),
                ('Susques','Susques'),('Tilcara','Tilcara'),('Tumbaya','Tumbaya'), ('Valle Grande','Valle Grande'),('Yavi','Yavi'))
    list_localidad = models.CharField(max_length=100,choices=localidad,default='Dr. Manuel Belgrano') 
    direccion_club = models.CharField(max_length=50)
    nombre_club = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    #id_categoria = models.ForeignKey(Categoria, null=False,blank=False,on_delete=models.CASCADE)#foranea
 
class Profesional(models.Model):
    dni_profesional = models.CharField(max_length=8, primary_key=True) 
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(default='valle@gmail.com')
     
    
    
    
""""
class Lugar(models.Model):
    id_lugar = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=35)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10) 
"""

class UsuarioActividad(models.Model): 
    dni_usuario = models.ForeignKey(Usuario, null=False,blank=False,on_delete=models.CASCADE)#foranea
    cod_actividad = models.ForeignKey(Actividad, null=False,blank=False,on_delete=models.CASCADE)

class ActividadProfesional(models.Model):
    dni_profesional = models.ForeignKey(Profesional, null=False,blank=False,on_delete=models.CASCADE)#foranea
    cod_actividad = models.ForeignKey(Actividad, null=False,blank=False,on_delete=models.CASCADE)

""""
class ActividadLugar(models.Model):
    cod_actividad = models.ForeignKey(Profesional, null=False,blank=False,on_delete=models.CASCADE)#foranea
    id_lugar = models.ForeignKey(Lugar, null=False,blank=False,on_delete=models.CASCADE)
"""
#DESPUES VOY A ADMIN.py PARA ADMINISTRAR MIS ENTIDADES
