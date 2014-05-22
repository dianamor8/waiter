# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from waiter.apps.usuarios.validators import *

class AutenticacionUsuario(AuthenticationForm):	
	AuthenticationForm.base_fields['username'].widget.attrs['class']='form-control'
	AuthenticationForm.base_fields['username'].widget.attrs['placeholder']='Usuario'
	AuthenticationForm.base_fields['password'].widget.attrs['class']='form-control'
	AuthenticationForm.base_fields['password'].widget.attrs['placeholder']='Contraseña'

    
class UserCreate(UserCreationForm):

	username = forms.RegexField (widget=forms.TextInput(attrs={'class':'form-control'}), label = "Nombre de usuario", max_length = 30, regex = r"^[\w'\.\-\_]+$", help_text = "Menor a 30 caracteres. Permitido: letras, dígitos y -._", error_messages = {'invalid': 'Contiene caracteres no permitidos.', 'required': 'Esta información es requerida.'} ,validators=[validarNuevoUsuario])
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'tucuenta@ejemplo.com'}),label='Correo electrónico', required=True, error_messages={'invalid': 'Ingrese una dirección de correo válida.', 'required': 'Esta información es requerida.'}, validators=[validarEmail])
	# Style CSS + Bootstrap
	UserCreationForm.base_fields['password1'].widget.attrs['class']='form-control'	
	UserCreationForm.base_fields['password2'].widget.attrs['class']='form-control'
	# Nombre de los labels para el form	
	UserCreationForm.base_fields['password1'].label='Contraseña'
	UserCreationForm.base_fields['password2'].label='Confirmación de Contraseña'

	UserCreationForm.base_fields['password1'].max_length=15
	UserCreationForm.base_fields['password2'].max_length=15
	# Texto de Ayuda para relleno de formularios	
	UserCreationForm.base_fields['password1'].widget.attrs['placeholder']='Registra una contraseña.'	
	UserCreationForm.base_fields['password2'].widget.attrs['placeholder']='Vuelve a escribir tu contraseña.'
	#Para informacion requerida	
	UserCreationForm.base_fields['password1'].error_messages={'required': 'Esta información es requerida.'}
	UserCreationForm.base_fields['password2'].error_messages={'required': 'Esta información es requerida.'}

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")		

	def clean_password1(self):
		datos = self.cleaned_data
		password1 = datos.get('password1')
		validarPassword1(password1)
		return password1
	
	def clean_password2(self):
		datos = self.cleaned_data		
		password1 = datos.get('password1')
		password2 = datos.get('password2')	
		if password1 is not None:			
			if password1!=password2:
				raise forms.ValidationError("Las contraseñas no coinciden.")		
		return password2
