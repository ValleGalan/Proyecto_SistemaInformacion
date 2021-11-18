from django.db import models

# Create your models here.
#creo mis entidades las que voy a usar en la BD
#sqlite 3 , no es necesario instalarse algo ya q es nativo

class Usuario(models.Model):
    cod_usuario = models.CharField(max_length=3, primary_key=True)
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    contrasena = models.CharField(max_length=30)
    correo_electronico = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)  # 3884040944
    edad = models.CharField(max_length=2)  # registran hasta 99años
#NOTA, falta tipo usuario, contraseña ver si es string o que

class Club(models.Model):
    cod_club = models.CharField(max_length=3, primary_key=True)
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    direccion = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)  # 3884040944

class Actividad(models.Model):
    cod_actividad = models.CharField(max_length=3, primary_key=True)
    apellido = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    tipo_actividad = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    modalidad = models.CharField(max_length=40)

class Profesional(models.Model):
    matricula = models.CharField(max_length=3, primary_key=True)
    apellido = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    correo_electronico = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=150)

class UsuarioActividad(models.Model):
    cod_usuario = models.ForeignKey(Usuario, null=False,blank=False,on_delete=models.CASCADE)#foranea
    cod_actividad = models.ForeignKey(Actividad, null=False,blank=False,on_delete=models.CASCADE)

class ActividadProfesional(models.Model):
    matricula = models.ForeignKey(Profesional, null=False,blank=False,on_delete=models.CASCADE)#foranea
    cod_actividad = models.ForeignKey(Actividad, null=False,blank=False,on_delete=models.CASCADE)

class ClubProfesional(models.Model):
    matricula = models.ForeignKey(Profesional, null=False,blank=False,on_delete=models.CASCADE)#foranea
    cod_club = models.ForeignKey(Club, null=False,blank=False,on_delete=models.CASCADE)

'''
class Estudiante(models.Model):
	dni = models.CharField(max_length=8,primary_key=True)
	apellidoPaterno = models.CharField(max_length=35)
	apellidoMaterno = models.CharField(max_length=35)
	nombres = models.CharField(max_length=35)
	fechaNacimiento = models.DateField()
	sexos = [('F','Femenino') , ('M','Masculino') ]
	sexo = models.CharField(max_length=1,choises=sexos,default='F')
	carrera = models.ForeignKey(Carrera, null=False,blank=False,on_delete=models.CASCADE)#foranea
	#on_delete=models.CASCADE me dice que si se borra un estudiante se van a borrar los estudiantes que dep de esa carrera
	#null=False  no puede ingresar nulo en la clave foranea
	vigencia =models.BooleanField(default=True) #defecto true

	def nombreCompleto(self): #nombre completo del estudiante
		txt ="{0} ,{1},{2}"
		return txt.format(self.apellidoPaterno,self.apellidoMaterno,self.nombres)

class Curso(models.Model):
	codigo = models.CharField(max_length=6,primary_key=True)
	nombre = models.CharField(max_length=30)
	creditos = models.PositiveSmallIntegerField()
	docente = models.CharField(max_length=100)

class Matricula(models.Model):
	id = models.AutoField(primary_key=True) #incremente solo !!
	estudiante= models.ForeignKey(Estudiante,null=False,blank=False,on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)
	fechaMatricula = models.DateTimeField(auto_now_add=True) #indica que se va a guardar con la fecha en la que se guarda el registro

#DESPUES VOY A ADMIN.py PARA ADMINISTRAR MIS ENTIDADES
'''