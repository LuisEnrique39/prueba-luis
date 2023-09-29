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
from django.core.paginator import  Paginator
from .models import Producto
from django.shortcuts import redirect


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
def produ(request):

  productos=Productos.objects.all()

      
  return render(request, 'social/productos.html', {"productos": productos})
def carrusel(request):

    return render(request, 'social/carrusel.html')

def consulta(request):
    
    info = Post.objects.all()
  
    context= {'posts': info}


    return render(request, 'social/consul.html', context)
def get(self,request,*args, **kwargs):
    if request.user.is_authenticated:
      return render(self.template_name)
    else:
      return redirect('login')


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


 #      self.request=request
   #     self.session=request.session
    #    carro=self.session.get("carro")

def compras(request):
  ejemplos = Producto.objects.all()
  print(request)
  if request.method == 'POST':  
       
        dato = tienda.objects.create(
                user_id=request.POST['Usuario'], 
                total=request.POST['total'],
        )
        dato.save()
  paginator = Paginator(ejemplos, 5)
  pagina = request.GET.get("page") or 1
  ejemplos = paginator.get_page(pagina) 
  pagina_actual = int(pagina)
  paginas = range(1, ejemplos.paginator.num_pages + 1)
 
  return render(request, 'social/tienda.html', {'ejemplos': ejemplos, "paginas": paginas, "pagina_actual": pagina_actual})

def carro(request):
    info = Producto.objects.all()
    ejemplo = tienda.objects.all()

    # Add pagination to 'ejemplo' queryset
    paginator = Paginator(ejemplo, 5)  # 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'social/consultaadmin.html', {'info': info, 'ejemplo': page_obj})

def carrous(request):
    info = tienda.objects.all()

    context= {'posts': info}


    return render(request, 'social/conultaus.html', context)
def carropro(request):
    # Get all objects from the 'tienda' model
    all_items = tienda.objects.all()

    # Set the number of items to display per page
    items_per_page = 10  # You can adjust this number as needed

    # Create a Paginator object
    paginator = Paginator(all_items, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    context = {'posts': page}
    return render(request, 'social/consultapro.html', context)
