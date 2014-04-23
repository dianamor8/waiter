from django.shortcuts import render
from django.template import RequestContext
from waiter.apps.producto.models import Producto
from waiter.apps.producto.forms import addProductForm
# Create your views here.

def productos_view(request):
	pro = Producto.objects.filter(estado=True)
	ctx = {'productos':pro}
	return render(request, 'producto/productos.html',ctx)

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
		return render(request,'producto/addProduct.html',ctx)
	else: #SI ES GET	
		formulario 	= addProductForm()
		ctx = {'formulario':formulario}
		return render(request,'producto/addProduct.html',ctx)