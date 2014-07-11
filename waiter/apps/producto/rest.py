 # -*- coding: utf-8 -*-
import json
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.forms.util import ErrorList
from django.http import HttpResponse, HttpResponseRedirect, Http404
from datetime import datetime,date

from waiter.apps.producto.forms import addCategoriaForm
from waiter.apps.producto.models import Categoria
from waiter.settings import LOGIN_URL, LOGIN_REDIRECT_URL

@login_required(login_url=LOGIN_URL)
def add_categorie_ajax(request):	
	if request.is_ajax():
		if request.method == 'POST':
			respuesta = False
			form_categorie = addCategoriaForm(request.POST)			
			if form_categorie.is_valid():
				# Verifica si ya existe una categoría con el mismo nombre								
				nombre= request.POST.get('nombre')
				categoriaExistente = Categoria.objects.filter(nombre=nombre)
				if not categoriaExistente:
					form_categorie.save()
					respuesta = True
					categorias = Categoria.objects.order_by('pk')
					lista = list()
					for cat in categorias:					
						lista.append({'tabla':'<tr id="tr%s"><td>%s</td><td>%s</td><td><a class="btn btn-success btn-xs call" data-target="#editCategorieModal%s"  data-toggle="modal" data-id="%s" data-nombre="%s"> <span class="glyphicon glyphicon-pencil"></span> Editar </a></td> <td><a class="btn btn-danger btn-xs delete" href="#deleteCategorieModal"  data-toggle="modal" role="button" data-id="%s" data-nombre="%s"><span class="glyphicon glyphicon-trash"></span> Eliminar</a> </td></tr>'%(cat.id, cat.id, cat.nombre, cat.id, cat.id, cat.nombre, cat.id, cat.nombre)})					
					ctx={'respuesta':respuesta, 'tabla':lista}
				else:
					listaErrores =list()
					listaErrores.append('Ya existe una categoría con ese nombre')
					ctx={'respuesta':respuesta, 'errores':listaErrores}
			else:
				errores = form_categorie.errors
				ctx={'respuesta':respuesta, 'errores':errores}
		return HttpResponse(json.dumps(ctx), content_type='application/json')	
	else:
		Http404

@login_required(login_url=LOGIN_URL)
def update_categorie_ajax(request):		
	if request.is_ajax():		
		if request.method == 'POST':			
			id_categoria = request.POST.get('id')			
			categoria = Categoria.objects.get(pk=id_categoria)						
			form_categorie = addCategoriaForm(request.POST)			
			respuesta = False				
			if form_categorie.is_valid():				
				nombre = form_categorie.cleaned_data['nombre']
				categoriaExistente = Categoria.objects.filter(nombre=nombre)
				# Verifica si al actualizar el nombre de la categoría ya existe					
				if categoriaExistente:					
					if int(categoriaExistente[0].id) == int(id_categoria):						
						categoria.nombre = nombre				
						categoria.save()				
						respuesta = True				
						categorias = Categoria.objects.order_by('pk')				
						lista = list() 
						for cat in categorias:					
							lista.append({'tabla':'<tr id="tr%s"><td>%s</td><td>%s</td><td><a class="btn btn-success btn-xs call" data-target="#editCategorieModal%s"  data-toggle="modal" data-id="%s" data-nombre="%s"> <span class="glyphicon glyphicon-pencil"></span> Editar </a></td> <td><a class="btn btn-danger btn-xs delete" href="#deleteCategorieModal"  data-toggle="modal" role="button" data-id="%s" data-nombre="%s"><span class="glyphicon glyphicon-trash"></span> Eliminar</a> </td></tr>'%(cat.id, cat.id, cat.nombre, cat.id, cat.id, cat.nombre, cat.id, cat.nombre)})
						ctx={'respuesta':respuesta, 'tabla':lista}
					else:
						listaErrores =list()
						listaErrores.append('No se puede actualizar, ya existe una categoria con ese nombre.')						
						ctx={'respuesta':respuesta, 'errores': listaErrores}
				else:
					categoria.nombre = nombre				
					categoria.save()				
					respuesta = True				
					categorias = Categoria.objects.order_by('pk')				
					lista = list() 
					for cat in categorias:					
						lista.append({'tabla':'<tr id="tr%s"><td>%s</td><td>%s</td><td><a class="btn btn-success btn-xs call" data-target="#editCategorieModal%s"  data-toggle="modal" data-id="%s" data-nombre="%s"> <span class="glyphicon glyphicon-pencil"></span> Editar </a></td> <td><a class="btn btn-danger btn-xs delete" href="#deleteCategorieModal"  data-toggle="modal" role="button" data-id="%s" data-nombre="%s"><span class="glyphicon glyphicon-trash"></span> Eliminar</a> </td></tr>'%(cat.id, cat.id, cat.nombre, cat.id, cat.id, cat.nombre, cat.id, cat.nombre)})
					ctx={'respuesta':respuesta, 'tabla':lista}			
			else:				
				errores = form_categorie.errors
				ctx={'respuesta':False, 'errores':errores}
		return HttpResponse(json.dumps(ctx), content_type='application/json')	
	else:
		Http404

@login_required(login_url=LOGIN_URL)
def delete_categorie_ajax(request):
	if request.method=="POST":
		if "categoria_id" in request.POST:
			try:
				categoria_id = request.POST['categoria_id']
				categoria = Categoria.objects.get(pk=categoria_id)
				mensaje = {"status":"True", "categoria_id":categoria.id}
				categoria.delete()
				return HttpResponse(json.dumps(mensaje), content_type='application/json')	
			except:
				mensaje = {"status":"False"}
				return HttpResponse(json.dumps(mensaje), content_type='application/json')	
				
			

			
		