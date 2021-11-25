from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from datetime import datetime #extraer la fecha
#from SI2021.Modulos.DeporteExtremo.models import Usuario
from DepNoConvencional.models import Profesional, Lugar ,Usuario
from django.views import generic #ListaUsuario
#-----------Envio de Email- en contactar
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from django.conf import Settings, settings
from django.core.mail import send_mail
#------------LOGIN
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
#from .forms import Login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#----------Formulario
from  DepNoConvencional.forms import LugarForm

# Plantillas Padres   SI2021.SI2021.DepNoConvencional.
def plantilla_base(request):
    return render(request,'plantilla_base.html')
def BaseLink(request):
    return render(request,'BaseLink.html')
def baseAdmin(request):
    return render(request,'baseAdmin.html')
#Plantillas de navegacion ,hijas
def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request,'inicio.html')
def nosotros(request):
    return render(request,'nosotros.html')

def deportesExtremos(request):
    return render(request,'deportesExtremos.html')

def disciplinasAlternativas(request):
    return render(request,'disciplinasAlternativas.html')

#Plantillas de administrador
 

#Plantillas para hacerlas funcionales 
def yoga(request):
    return render(request,'yoga.html')
def ubicacion(request):
    return render(request,'ubicacion.html')

def registro(request):
    return render(request,'registro.html')

def ListaModificar(request):
    return render(request,'ListaModificar.html')
 
#Plantillas para login
''' FECHA DEL SISTEMA
def login(request):
    #fecha del sistema
    data_today=datetime.now().date() # 
    return render(request,'login.html',{'data_today':data_today}) 
'''
@login_required
def login(request):
    return render(request,'login.html')
def salir(request):
    logout(request)
    return redirect('/')
'''
def login(request):
    #fecha del sistema
    form=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None and user.is_director==False:
            login(request,user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('login') #si entro va a 
    return render(request,'login.html',{'form':form})
'''

def perfil(request):
    return render(request,'perfil.html')
def registro(request):
    return render(request,'registro.html')
#------------Peticiones
def mensaje(request):
    return HttpResponse('!Hola desde Django!')
#------------Formulario agregar actividad-lugar
def agregarLUG(request):
    #form= Lugar()
    if request.method == 'POST':
        fm=LugarForm(request.POST)
        if fm.is_valid():
            print("valido")
            #lugar = Lugar()
            #lugar.id_lugar = form.cleaned_data['id_lugar']
            #lugar.nombre = form.cleaned_data['nombre']
            #lugar.localidad = form.cleaned_data['localidad']
            #lugar.direccion = form.cleaned_data['direccion']
            #lugar.telefono = form.cleaned_data['telefono']
            fm.save()
            return redirect('/sumarActividad')
    else:
            print("invalido")
            fm = LugarForm()
    return render(request,'sumarActividad.html',{'form':fm})


#-----------Consultar datos ,FILTROS DE LUGAR POR ACTIVIDAD
def ListaModificar(request):
    list_user = Usuario.objects.filter(rol__exact="user") #presentar nuestros usuarios
    context = {'lista_Usuarios': list_user} #var donde guardo la lista
    return render(request,'ListaModificar.html', context)

def listaProfesional(request):
    list_profesional = Profesional.objects.filter()  
    context = {'lista_PROF': list_profesional} #var donde guardo la lista
    return render(request,'ListaModificar.html', context)

def listaLugar(request):
    list_lugar = Lugar.objects.filter()  
    context = {'lista_LUGAR': list_lugar}  
    return render(request,'yoga.html', context)
#--------------Funcion 
def ContadorUsuario(request):
    """ Función vista para la página inicio del sitio """
    # Genera contadores de algunos de los objetos principales
    num_usuario=Usuario.cod_usuario.objects.all().count()
    #num_instances=Usuario.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=Usuario.nombre.objects.filter(nombre__exact='a').count()
    num_apellido=Usuario.apellido.objects.count()  # El 'all()' esta implícito por defecto.
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'ListaModificar.html',
        context={'num_usuario':num_usuario,'num_instances_available':num_instances_available,'num_apellido':num_apellido},
    )
#------------Conteos de Visita
'''
def ListaModificar(request):
    # Genera contadores de algunos de los objetos principales
    nombre=Usuario.objects.all().count()
    num_instances=Usuario.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=Usuario.nombre.objects.filter(nombre__exact='L').count()
    num_authors=Usuario.objects.count()  # El 'all()' se obvia en este caso.
    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'nombre':nombre,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_visits':num_visits,
    } 

    # Carga la plantilla index.html con la información adicional en la variable context.
    return render(request, 'ListaModificar.html', context=context)
'''
#-------------Para la vista
class ListaUsuario(generic.ListView):
    model = Usuario
#-------------Formulario contacto-enviar gmail
'''def contactar(request):
    return render(request,'contactar.html')
def send_email(mail):
    context={'mail':mail}
    template=get_template('ListaModificar.html') #para comprobar el envio
    content =template.render(context)
    email=EmailMultiAlternatives(
        'un correo de prueba',
        'Flor Galan',
        settings.EMAIL_HOST_USER, #configure en setting
        [mail]
    )'''
    
def contactar(request):
    if request.method =='POST':
        nombre=request.POST["nombre"]
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["vallegalan810@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)              
    return render(request,'contactar.html')
#-------------Sesion
'''
# Obtener un dato de la sesión por su clave (ej. 'my_car'), generando un KeyError si la clave no existe
my_car = request.session['my_car']

# Obtener un dato de la sesión, estableciendo un valor por defecto ('mini') si el dato requerido no existe
my_car = request.session.get('my_car', 'mini')

# Asignar un dato a la sesión
request.session['my_car'] = 'mini'

# Eliminar un dato de la sesión
del request.session['my_car']
# Esto es detectado como un cambio en la sesión, así que la información de la sesión es guardada.
request.session['my_car'] = 'mini' '''

#-------------Para el administrador


