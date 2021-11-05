from django.contrib import admin

from Modulos.DeporteExtremo.models import *
# Register your models here.
#LOS MODELOS que cree ,para administrarlos en panel de admin,registrar las entidades
admin.site.resgister(Usuario)
admin.site.resgister(Club)
dmin.site.resgister(Actividad)
admin.site.resgister(Profesional)
admin.site.resgister(UsuarioActividad)
dmin.site.resgister(ActividadProfesional)
admin.site.resgister(ClubProfesional)

