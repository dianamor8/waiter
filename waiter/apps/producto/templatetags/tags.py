# -*- coding:utf-8 -*-
from django import template
from waiter.apps.producto.forms import addCategoriaForm,addAreaProduccionForm
from waiter.apps.producto.models import Categoria, AreaProduccion

register = template.Library()

@register.inclusion_tag('producto/categorie/add_categorie_form.html', takes_context=True)
# @register.filter(name='addcss')
def add_categoria(context, pk=None):
	form = addCategoriaForm()
	if pk is not None:		
		categoria = Categoria.objects.filter(id=pk)
		if categoria:
			categoria = Categoria.objects.get(id=pk)		 	
			form = addCategoriaForm(instance=categoria)		
	form.fields['nombre'].widget.attrs = {'class':'form-control'}
	contexto = {'form_add_categoria': form}
	return contexto


@register.inclusion_tag('producto/productionArea/add_production_area_form.html', takes_context=True)
# @register.filter(name='addcss')
def add_area(context, pk=None):	
	form = addAreaProduccionForm()	
	if pk is not None:				
		area = AreaProduccion.objects.filter(id=pk)
		if area:			
			area = AreaProduccion.objects.get(id=pk)		 				
			form = addAreaProduccionForm(instance=area)		
			
	form.fields['nombre'].widget.attrs = {'class':'form-control'}	
	contexto = {'form_add_production_area': form}	
	return contexto