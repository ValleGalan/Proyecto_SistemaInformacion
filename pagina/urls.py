from django.urls import path
#from django.urls.resolvers import URLPattern
from PROYECTO_SISTEMAINFORMACION import view 

urlspatterns =[
    path ('busqueda/', view.busqueda),
    
]