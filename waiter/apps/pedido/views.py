from django.shortcuts import render
from django.template import RequestContext
from waiter.apps.pedido.models import Pedido, ESTADO_CHOICES, ItemPedido 
#from waiter.apps.pedido.forms import addPedidosForm


def pedido_view(request):	
	ped=Pedido.objects.all()
	ctx={'pedido':ped}
	return render(request,'pedido/order.html',ctx)

# Create your views here.
