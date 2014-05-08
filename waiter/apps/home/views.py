from django.shortcuts import render, render_to_response
from django.template import RequestContext
from waiter.apps.home.forms import ContactForm, LoginForm
from django.core.mail import EmailMultiAlternatives #Enviamos html
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

# Create your views here.

#Vista con render_to_response
#def index_view(request):
#	return render_to_response('home/index.html', context_instance = RequestContext(request))

#Vista con render
def index_view(request):
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


def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponserRedirect('/')
	else:
		if(request.method == "POST"):
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data["username"]
				password = form.cleaned_data["password"]
				usuario = authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o password incorrecto"
		form = LoginForm()
		ctx = {'form':form, 'mensaje':mensaje}
		return render(request, "home/login.html", ctx)

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')