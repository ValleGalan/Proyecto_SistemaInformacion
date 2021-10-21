from django.shortcuts import render

# acá se crean las vistas

def busqueda(request):
    return render(request, "busqueda.html")