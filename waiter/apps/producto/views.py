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
		return render(request, 'producto/products.html',ctx)
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
			return render(request,'producto/addProduct.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def add_categorie_view(request):	
	mensaje=""
	if request=="POST":
		CategorieForm = addCategoriaForm(request)
		if CategorieForm.is_valid():
			CategorieForm.save()
			print "##paso aqui"
			return HttpResponseRedirect("producto/categories.html")			
		else:
			mensaje = "El formulario contiene errores."
	print "aqui"
	CategorieForm = addCategoriaForm()
	context= {'CategorieForm':CategorieForm, 'mensaje':mensaje}
	return render(request, "producto/categories.html", context)

@login_required(login_url=LOGIN_URL)
def categories_view(request):
	if request.user.is_authenticated():
		cat= Categoria.objects.all()
		ctx= {'categorias':cat}
		return render(request,'producto/categories.html',ctx)
	else:
		return HttpResponseRedirect(LOGIN_REDIRECT_URL)

@login_required(login_url=LOGIN_URL)
def areas_de_produccion_view(request):
	if request.user.is_authenticated():	
		areas= AreaProduccion.objects.all()
		ctx= {'areas':areas}
		return render(request,'producto/areas.html',ctx)
	else:
		return HttpResponseRedirect('/')
	

		
