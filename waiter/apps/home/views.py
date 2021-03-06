from django.shortcuts import render, render_to_response
from django.template import RequestContext
from waiter.apps.home.forms import ContactForm, LoginForm
from django.core.mail import EmailMultiAlternatives #Enviamos html
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from waiter.settings import LOGIN_URL, LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from waiter.apps.producto.models import Producto

# Create your views here.

#Vista con render_to_response
#def index_view(request):
#	return render_to_response('home/index.html', context_instance = RequestContext(request))

#Vista con render
def index_view(request):
	if request.user.is_authenticated():
		return render(request, 'home/inicio.html')
	else:		
		# Se redirecciona al carousel
		return render(request, 'home/index.html')

def carousel_view(request):
	return render(request, 'base/carousel.html')

def about_view(request):
	mensaje = "A cerca de.."
	ctx = {'msg':mensaje}
	return render(request, 'home/about.html',ctx)

def contact_view(request):	
	info_enviado = False
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			#######
			#CONFIGURACION DE MENSAJE GMAIL
			to_admin= "mp.dianalexa@gmail.com"
			html_content = "Informacion recibida <br> MENSAJE <br> %s"%(texto)
			msg = EmailMultiAlternatives('Correo de contacto', html_content,'from@server.com', [to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
			#######
	else:
		formulario = ContactForm()
	ctx = {"form":formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
	return render(request, "home/contact.html",ctx)

@login_required(login_url=LOGIN_URL)
def panel_administracion_view(request):
	ctx= {'sidebar':'administracion'}
	return render(request, 'home/panel_administracion/panel_administracion.html', ctx)

@login_required(login_url=LOGIN_URL)
			#CONFIG
def configurations_view(request):	
	ctx= {'sidebar':'administracion'}
	return render(request, 'home/panel_administracion/configurations.html',ctx)