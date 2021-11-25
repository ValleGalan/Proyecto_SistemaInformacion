from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpRequest

class FormularioUsuario(HttpRequest):
    def login(request):
        usuario=FormularioUsuario()
        return render(request,"inicio.html",{"form":usuario})
    ''' 
    del procesar_formulario(request): #validacion
        usuario=FormularioUsuario()
        if usuario.is_valid():
            usuario.save()
            usuario=FormularioUsuario()
    return render (request,"login.html",{"form":usuario,"mensaje":'OK'})
      '''  
        
