from django import template
from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse 
from datetime import datetime #extraer la fecha
#from SI2021.Modulos.DeporteExtremo.models import Usuario
from DepNoConvencional.models import Actividad, Profesional ,Usuario
from django.views import generic #ListaUsuario
#-----------Envio de Email- en contactar
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import  settings
from django.core.mail import send_mail
#--------------Paginador
from django.core.paginator import Page, Paginator
from django.http import Http404
#------------LOGIN
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import authenticate,login,logout
#from .forms import Login
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required
#----------Formulario
from  DepNoConvencional.forms import ActividadForm ,ProfesionalForm

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

def ubicacion(request):
    return render(request,'ubicacion.html')

def registro(request):
    return render(request,'registro.html')




#Plantillas para login
''' FECHA DEL SISTEMA 
def login(request):
    #fecha del sistema
    data_today=datetime.now().date() # 
    return render(request,'login.html',{'data_today':data_today}) 
'''

'''
@login_required
def login(request):
    return render(request,'login.html')
def salir(request):
    logout(request)
    return redirect('/')

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
 
#------------Peticiones
def mensaje(request):
    return HttpResponse('!Hola desde Django!')
#------------Formulario ACTIVIDAD -CRUD
def agregar_actividad(request):
    if request.method == 'POST':
        fm=ActividadForm(request.POST)
        if fm.is_valid():
            print("valido")
            fm.save()
            return redirect('/agregar')
    else:
            print("invalido es el formulario ")
            fm = ActividadForm()
    return render(request,'agregar.html',{'form':fm})

def eliminar(request, cod_actividad):
    act = get_object_or_404(Actividad,cod_actividad=cod_actividad)
    act.delete()
    return redirect(to="lista_actividad")

def modificar(request, cod_actividad):
    act = get_object_or_404(Actividad,cod_actividad=cod_actividad) #buscar(modelo,condicion)
    data= { 
           'form'  : ActividadForm(instance=act)
           }
    if request.method == 'POST':
        formulario= ActividadForm(data=request.POST ,instance= act,files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='lista_actividad')
        data['form'] = formulario      
        
    return render(request,'modificar.html', data)
def agregar_profesional(request):
    if request.method == 'POST':
        fm=ProfesionalForm(request.POST)
        if fm.is_valid():
            print("valido")
            fm.save()
            return redirect('/agregar_profesional')
    else:
            print("invalido es el formulario ")
            fm = ProfesionalForm()
    return render(request,'agregar_profesional.html',{'forms':fm})
 
def eliminar_pro(request, dni_profesional):
    act = get_object_or_404(Profesional,dni_profesional=dni_profesional)
    act.delete()
    return redirect(to="lista_profesional")

def modificar_pro(request, dni_profesional):
    act = get_object_or_404(Profesional,dni_profesional=dni_profesional) #buscar(modelo,condicion)
    data= { 
           'forms'  : ProfesionalForm(instance=act)
           }
    if request.method == 'POST':
        formulario= ProfesionalForm(data=request.POST ,instance= act,files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='lista_profesional')
        data['forms'] = formulario      
        
    return render(request,'modificar_pro.html', data)
'''
def modificarAct (request,cod_actividad):
    Activida= Actividad.objects.filter(cod_actividad=cod_actividad).first()
    form = ActividadForm(instance= Activida)
    return render(request, "modificar.html" ,{"form" : form,'Actividad':Activida})
'''  
#-----------Consultar datos ,FILTROS DE LUGAR POR ACTIVIDAD
def ListaUsuario(request):
    list_user = Usuario.objects.filter(rol__exact="user") #presentar nuestros usuarios
    context = {'lista_Usuarios': list_user} #var donde guardo la lista
    return render(request,'ListaModificar.html', context)
 
def listaAProfesional(request):
    list_profesional = Profesional.objects.filter()  
    context = {'lista_PROF': list_profesional} #var donde guardo la lista
    return render(request,'ListaProfesional.html', context)

def listaProfesional(request):  #paginador
    list_act = Profesional.objects.all()
    page= request.GET.get('page',1)
    try:
        paginator = Paginator(list_act,5) #cantidad que listo
        list_act = paginator.page(page)
    except:
        raise Http404
    data = {'entity': list_act,
            'paginator': paginator }  
    return render(request,'lista_profesional.html', data)

def listAActividad(request):  #comun
    list_act = Actividad.objects.all()
    context = {'lista_ACTIVIDAD': list_act}  
    return render(request,'lista_actividad.html', context)

def listActividad(request):  #paginador
    list_act = Actividad.objects.all()
    page= request.GET.get('page',1)
    try:
        paginator = Paginator(list_act,5) #cantidad que listo
        list_act = paginator.page(page)
    except:
        raise Http404
    data = {'entity': list_act,
            'paginator': paginator }  
    return render(request,'lista_actividad.html', data)

def listActividadYoga(request):
    list_act = Actividad.objects.filter(list_actividad__exact="yoga") #presentar nuestros usuarios
    context = {'lista_ACTIVIDAD': list_act} #var donde guardo la lista
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


