# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from waiter.apps.conexiones.models import Conexion, CONEXION_CHOICES, ConexionDB

class addConexionDataBaseForm(forms.Form):		
	fuente = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class':'form-control'}),choices=CONEXION_CHOICES)	
	def clean(self):
		return self.cleaned_data

class TypeConexionForm(forms.ModelForm):
	class Meta:		
		model = Conexion
		fields = ('fuente',)
		error_messages = {
			'fuente': {
				'required': u"Seleccione una opción.",
				'invalid_choice': u"Selección inválida.",
			},
		}	
		widgets = {
			'fuente': forms.Select(attrs={'class':'form-control'}),
		}
		labels ={
			'fuente' : 'Fuente de Datos:',
		}

class ConexionDBForm(forms.ModelForm):
	class Meta:        
		model = ConexionDB
		fields = ("gestor", "database", "userdb", "passworddb", "host", "port")
		labels = {
			'gestor': ('Gestor de Base de Datos:'),
			'database': ('Base de Datos:'),
			'userdb': ('Usuario:'),
			'passworddb': ('Contraseña:'),
			'host': ('Host:'),
			'port': ('Puerto:'),
		}
		error_messages = {		
			'gestor': {
				'invalid_choice': u"Selección inválida.",
			},
			'database': {
				'required': u"Este valor no puede estar vacío.",
			},
			'userdb': {
				'required': u"Este valor no puede estar vacío.",
			},
			'host': {
				'required': u"Este valor no puede estar vacío.",
				'invalid': u"No es una dirección válida.",
			},
			'port': {
				'required': u"Este valor no puede estar vacío.",
			},
		}
		widgets = {
			'gestor': forms.Select(attrs={'class':'form-control'}),
			'database': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la base de datos.'}),
			'userdb': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario de la base de datos.'}),
			'passworddb': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña de acceso.'}),
			'host': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección host del equipo.'}),
        	'port': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Puerto de conexión.'}),            
		}