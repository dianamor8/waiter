# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from waiter.apps.producto.models import ESTADO_CHOICES, AreaProduccion, Categoria

class addProductForm(forms.Form):
	codigo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	precio = forms.DecimalField(decimal_places=2)
	estado = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class':'form-control'}),choices=ESTADO_CHOICES)
	categoria = forms.ModelChoiceField(queryset= Categoria.objects.all(), required=True)
	area_de_produccion = forms.ModelChoiceField(queryset= AreaProduccion.objects.all(), required=True)
	imagen = forms.ImageField(required=False)
	def clean(self):
		return self.cleaned_data

class addCategoriaForm(ModelForm):	
	class Meta:
		model = Categoria
		error_messages = {
            'nombre': {            	
            	'required': u"Este valor no puede estar vacío.",
            },
        }		
	
class addAreaProduccionForm(ModelForm):	
	class Meta:
		model = AreaProduccion
		error_messages={
			'nombre':{
				'required': u"Este valor no puede estar vacío.",
			},
		}