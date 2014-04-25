from django.shortcuts import render
from django.template import RequestContext
from waiter.apps.producto.models import Producto, ESTADO_CHOICES, Categoria
from waiter.apps.producto.forms import addProductForm

# Create your views here.
# Nombres de views en ingles

def products_view(request):
	activo = ESTADO_CHOICES[0][0]
	no_activo = ESTADO_CHOICES[1][0]
	pro = Producto.objects.filter(estado=activo)
	ctx = {'productos':pro}
	return render(request, 'producto/products.html',ctx)

def add_product_view(request):
	if request.method == "POST":
		formulario = addProductForm(request.POST)
		info = "Inicializando"
		if formulario.is_valid():
			codigo= formulario.cleaned_data['codigo']			
			nombre= formulario.cleaned_data['nombre']
			precio= formulario.cleaned_data['precio']
			estado= formulario.cleaned_data['estado']
			categoria = formulario.cleaned_data['categoria']
			areaProduccion = formulario.cleaned_data['area_de_produccion']
			p = Producto()
			p.codigo = codigo
			p.nombre = nombre
			p.precio = precio
			p.estado = estado
			p.categoria = categoria
			p.areaProduccion = areaProduccion
			p.save()
			info = "Se guardo satisfactoriamente"
		else:
			info = "Informacion con datos incorrectos"
		formulario 	= addProductForm()
		ctx = {'formulario':formulario,'informacion':info}
		return render(request,'producto/agregarProducto.html',ctx)
	else: #SI ES GET	
		formulario 	= addProductForm()
		ctx = {'formulario':formulario}
<<<<<<< HEAD
		return render(request,'producto/addProduct.html',ctx)

def categories_view(request):
	categorias= Categoria.objects.filter(id=1)
	ctx= {'categorias':categorias}
	return render(request,'producto/categories.html',ctx)

	
=======
		return render(request,'producto/agregarProducto.html',ctx)
>>>>>>> b7636c699d5318ec8f5ae633eeec9fd52a3331e0
