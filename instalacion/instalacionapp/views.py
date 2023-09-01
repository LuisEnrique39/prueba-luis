from re import template
from django.shortcuts import render, redirect
from .models import *
from .models import Post
from .models import Usuario
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden
from .models import tienda
from .models import Producto

#django nos permite tener forms#


# Create your views here.
# el context es para pedir datos a base 

def feed(request):
 
  return render(request, 'social/feed.html')


def perfil(request):
 
  return render(request, 'social/perfil.html')

 
def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('feed')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/registro.html', context)



 


def login(request):
 
  return render(request, 'social/login.html')

@login_required
def retorno(request):
 
  return render(request, 'social/prueba.html')

def contacto(request):
  template = 'instalacionapp/contacto.html'
  if request.method == 'POST':  
       
        dato = Post.objects.create(
          
                user_id=request.POST['usuario'], 
                id_propiedad=request.POST['id_propiedad'], 
                tipo_propiedad=request.POST['tipo_propiedad'], 
                ubicacion=request.POST['ubicacion'], 
                metros_cuadrados=request.POST['metros_cuadrados'], 
                renta_o_venta=request.POST['renta_o_venta'], 
                precio=request.POST['precio'], 
                n_habitaciones=request.POST['n_habitaciones'],  
                estado_habitaciones=request.POST['estado_habitaciones'], 
                disponible=request.POST['disponible'], 

          )
        dato.save()
  return render(request, 'social/contacto.html')

def carrusel(request):
 
  return render(request, 'social/carrusel.html')

def consulta(request):
    
    info = Post.objects.all()
  
    context= {'posts': info}


    return render(request, 'social/consul.html', context)

def correo(request):
      
  if request.method == 'POST':  
        correoPru=request.POST['correo']
        asunto= request.POST['nombre']+ ' '+ request.POST['apellidos']+ ', '+ request.POST['fecha']+ ' con asunto '+ request.POST['asunto']+ ' con correo '+ request.POST['correo']+ ' \n ' +'Envio su informacion para una consulta con respecto al comentario: '+ request.POST['comentarios']+ ' \n '+ 'En breve sera contactado ' 
        dato = Usuario.objects.create(
            nombre=request.POST['nombre'], 
            apellidos=request.POST['apellidos'], 
            fecha=request.POST['fecha'], 
            asunto=request.POST['asunto'],
            correo=request.POST['correo'],
            comentarios=request.POST['comentarios']
            )
        dato.save()
        
        send_mail(
    'Correo de Confirmacion',
    asunto,
    'HOLA',
    [correoPru,'luiscruznoguez39425@gmail.com'],
    fail_silently=False
)
  context = {}
  return render(request, 'social/ema.html')

def compras(request):
  ejemplos = Producto.objects.all()
  print(request)
  if request.method == 'POST':  
       
        dato = tienda.objects.create(
          
                user_id=request.POST['Usuario'], 
                nombre=request.POST['Nombre'], 
                apellido=request.POST['Apellidos'], 
                correo=request.POST['Correo'], 
                numero=request.POST['Numero'],
                pago=request.POST['metodo_pago'],
                total=request.POST['total'],

                
				
               
            
          )
        dato.save()
  return render(request, 'social/tienda.html', {'ejemplos' :ejemplos})





#def consultapr(request, username=None):
#    l = Producto.objects.all()
    
 #   current_user = request.user
  #  if username and username != current_user.username:
   #     user = User.objects.get(username=username)
    #else:
     #   user = current_user
    #return render(request, 'social/consultapro.html', {'user': user,'l' :l})
