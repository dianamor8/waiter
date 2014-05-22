from django.shortcuts import render
from django.http import HttpResponse
from waiter.apps.producto.models import Producto, ESTADO_CHOICES

# Create your views here.

#Integramos la serializacion 
from django.core import serializers

#EN FORMATO JSON
def ws_Products_view(request):
	activo = ESTADO_CHOICES[0][0]
	data = serializers.serialize("xml", Producto.objects.filter(estado=activo))
	return HttpResponse(data, mimetype="application/xml")