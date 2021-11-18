from django.shortcuts import render

# inicio PLANTILLAS
def plantilla_base(request):
    return render(request,'plantilla_base.html')

def BaseLink(request):
    return render(request,'BaseLink.html')

def ListaModificar(request):
    return render(request,'ListaModificar.html')

def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request,'inicio.html')


def login(request):
    return render(request,'login.html')

def nosotros(request):
    return render(request,'nosotros.html')

def usuario(request):
    return render(request,'usuario.html')

def deportesExtremos(request):
    return render(request,'deportesExtremos.html')

def disciplinasAlternativas(request):
    return render(request,'disciplinasAlternativas.html')

def yoga(request):
    return render(request,'yoga.html')
def perfil(request):
    return render(request,'perfil.html')

 
#fin PLANTILLAS