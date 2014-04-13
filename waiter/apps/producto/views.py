from django.shortcuts import render
from django.template import RequestContext
from waiter.apps.producto.models import Producto
# Create your views here.

def productos_view(request):
	pro = Producto.objects.filter(estado=True)
	ctx = {'productos':pro}
	return render(request, 'producto/productos.html',ctx)

