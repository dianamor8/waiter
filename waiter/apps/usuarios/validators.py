# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from waiter.apps.home.util import * 
from django.contrib.auth.models import User
from django import forms

def validarUsuario(value):
	user = User.objects.filter(username=value)
	if not tamanio_min(value, 3):
		raise forms.ValidationError("El nombre de usuario debe contener al menos 3 caracteres.")
	if user:
		raise forms.ValidationError("Este usuario no está disponible.")

def validarEmail(value):
	user = User.objects.filter(email=value)
	if user:
		raise forms.ValidationError("Lo sentimos. Al parecer %s ya es usada por otra cuenta."%value)

def validarPassword1(value):
	if not tamanio_min(value, 6):
		raise forms.ValidationError("Tu contraseña debe tener al menos 6 caracteres.")
	
