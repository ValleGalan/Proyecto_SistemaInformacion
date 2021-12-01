from django.contrib import admin
 
from DepNoConvencional.models import *

# LOS MODELOS que cree ,para administrarlos en panel de admin,registrar las entidades
admin.site.register(Usuario)
admin.site.register(Actividad)
#admin.site.register(Lugar)
admin.site.register(Profesional)

#admin.site.register(ActividadUsuario)
admin.site.register(ActividadProfesional)
#admin.site.register(ActividadLugar)

#-------------Para el administrador 
'''
from django.contrib import admin
from DepNoConvencional.models import Author

admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)'''

