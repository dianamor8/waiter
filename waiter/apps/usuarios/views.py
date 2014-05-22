# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from waiter.apps.usuarios.forms import AutenticacionUsuario, UserCreate
from django.contrib.auth.decorators import login_required
from waiter.settings import LOGIN_URL, LOGIN_REDIRECT_URL
from django.contrib.auth.models import User


# Create your views here.

def forms_view(request):
	mensaje=""
	if request.user.is_authenticated():
		return HttpResponseRedirect(LOGIN_REDIRECT_URL)
	else:
		if request.method=="GET":
			formAutenticacion = AutenticacionUsuario()
			#formRegistro = RegistroUsuario()
			formRegistro = UserCreate()
		else:
			formAutenticacion = AutenticacionUsuario(data=request.POST, request=request)
			#formRegistro = RegistroUsuario(request.POST)
			formRegistro = UserCreate(request.POST)
			if formAutenticacion.is_valid():
				return login_view(request)
			if formRegistro.is_valid():
				return create_user_cliente_view(request)
		ctx = {'LoginForm':formAutenticacion, 'CreateForm':formRegistro, 'mensaje':mensaje}
		return render(request, "usuarios/login.html", ctx)



def login_view(request):
	mensaje =""
	if request.user.is_authenticated():
		return HttpResponseRedirect(LOGIN_REDIRECT_URL)
	else:
		if(request.method == "POST"):			
			form = AutenticacionUsuario(data=request.POST, request=request)						
			if form.is_valid():				
				username = form.cleaned_data["username"]
				password = form.cleaned_data["password"]				
				usuario = authenticate(username=username, password=password)				
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect(LOGIN_REDIRECT_URL)
				else:
					mensaje = "usuario y/o password incorrecto"
		form = AutenticacionUsuario()
		ctx = {'LoginForm':form, 'mensaje':mensaje}
		return render(request, "usuarios/login.html", ctx)

@login_required(login_url=LOGIN_URL)
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(LOGIN_REDIRECT_URL)



def create_user_cliente_view(request):
	mensaje = ""		
	form = UserCreate(request.POST)
	# para crear el grupo por defecto http://python.majibu.org/preguntas/1131/crear-grupo-y-asignar-permisos-sin-la-interfaz-admin
	if form.is_valid():
		username = form.clean_username()
		password = form.clean_password2()
		form.save() #retorna el model del objeto a guardar
		user = authenticate(username=username,password=password)
		login(request, user)
		return HttpResponseRedirect(LOGIN_REDIRECT_URL)
	else:
		mensaje = "La información requerida tiene datos incorrectos."	
	ctx = {'CreateForm':form, 'mensaje':mensaje}
	return render(request, 'usuarios/login.html', ctx)