# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from waiter.apps.producto.models import Producto, ESTADO_CHOICES, Categoria, AreaProduccion
from waiter.apps.producto.forms import addProductForm, addCategoriaForm
from django.http import HttpResponseRedirect
from waiter.settings import LOGIN_URL, LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required

# Create your views here.
# Nombres de views en ingles

def products_view(request):
	if request.user.is_authenticated():	
		activo = ESTADO_CHOICES[0][0]
		no_activo = ESTADO_CHOICES[1][0]
		pro = Producto.objects.filter(estado=activo)
		ctx = {'productos':pro}
		return render(request, 'producto/product/products.html',ctx)
	else:
		return HttpResponseRedirect('/')
	

def add_product_view(request):
	if request.user.is_authenticated():	
		if request.method == "POST":
			formulario = addProductForm(request.POST, request.FILES)
			info = "Inicializando"
			if formulario.is_valid():
				codigo= formulario.cleaned_data['codigo']			
				nombre= formulario.cleaned_data['nombre']
				precio= formulario.cleaned_data['precio']
				imagen= formulario.cleaned_data['imagen'] # esto se obtiene con el request.FILES
				estado= formulario.cleaned_data['estado']
				categoria = formulario.cleaned_data['categoria']
				areaProduccion = formulario.cleaned_data['area_de_produccion']
				p = Producto()
				p.codigo = codigo
				p.nombre = nombre
				p.precio = precio
				p.estado = estado
				if imagen:
					p.imagen = imagen
				p.categoria = categoria
				p.areaProduccion = areaProduccion
				p.save()
				info = "Se guardo satisfactoriamente"
			else:
				info = "Informacion con datos incorrectos"
			formulario 	= addProductForm()
			ctx = {'formulario':formulario,'informacion':info}
			return render(request,'producto/addProduct.html',ctx)
		else: #SI ES GET	
			formulario 	= addProductForm()
			ctx = {'formulario':formulario}
			return render(request,'producto/product/add_product.html',ctx)
	else:
		return HttpResponseRedirect('/')


@login_required(login_url=LOGIN_URL)
def categories_view(request):
	if request.user.is_authenticated():
		cat= Categoria.objects.order_by('pk')
		ctx= {'categorias':cat}
		print "pasa categorias"
		return render(request,'producto/categorie/categories.html',ctx)
	else:
		return HttpResponseRedirect(LOGIN_REDIRECT_URL)

@login_required(login_url=LOGIN_URL)
def areas_de_produccion_view(request):
	if request.user.is_authenticated():	
		areas= AreaProduccion.objects.order_by('pk')
		ctx= {'areas':areas}
		return render(request,'producto/productionArea/productionAreas.html',ctx)
	else:
		return HttpResponseRedirect(LOGIN_REDIRECT_URL)
	
def areasjairo(request):
	return render(request,'producto/areas.html')

	

@login_required(login_url=LOGIN_URL)
def categories_product_view(request, id_categorie=None):
	categories = Categoria.objects.order_by('nombre')
	if id_categorie is None:
		if categories:
			categorieaux = categories[0]
			id_categorie= int(categorieaux.id)
			products = Producto.objects.filter(categoria=id_categorie).order_by('nombre')	
			ctx = {'id_categorie': int(id_categorie), 'products':products, 'categories':categories}
		else:
			mensaje= "Aún no hay categorías registradas."
			ctx = {'mensaje':mensaje}						
	else:
		products = Producto.objects.filter(categoria=id_categorie).order_by('nombre')	
		ctx = {'id_categorie': int(id_categorie), 'products':products, 'categories':categories}
	return render(request, 'producto/categorie/categories_products.html', ctx)
		
