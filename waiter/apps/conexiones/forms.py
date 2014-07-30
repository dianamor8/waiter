# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from waiter.apps.conexiones.models import Conexion, CONEXION_CHOICES

class addConexionDataBaseForm(forms.Form):		
	fuente = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class':'form-control'}),choices=CONEXION_CHOICES)	
	def clean(self):
		return self.cleaned_data