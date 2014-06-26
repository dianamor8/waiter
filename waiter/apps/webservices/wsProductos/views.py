from django.shortcuts import render
from django.http import HttpResponse
from waiter.apps.producto.models import Producto, ESTADO_CHOICES, Categoria, AreaProduccion

# Create your views here.

#Integramos la serializacion 
from django.core import serializers

#EN FORMATO JSON
def ws_Products_view_js(request):
	activo = ESTADO_CHOICES[0][0]
	data = serializers.serialize("json", Producto.objects.filter(estado=activo))
	return HttpResponse(data, content_type="application/json")

def ws_Products_view_xml(request):
	activo = ESTADO_CHOICES[0][0]
	data = serializers.serialize("xml", Producto.objects.filter(estado=activo))
	return HttpResponse(data, content_type="application/xml")

def ws_Categories_view_js(request):	
	data = serializers.serialize("json", Categoria.objects.all())
	return HttpResponse(data, content_type="application/json")

def ws_Categories_view_xml(request):	
	data = serializers.serialize("xml", Categoria.objects.all())
	return HttpResponse(data, content_type="application/xml")


def ws_AreaProduccion_view_js(request):	
	data = serializers.serialize("json", AreaProduccion.objects.all())
	return HttpResponse(data, content_type="application/json")

def ws_AreaProduccion_view_xml(request):	
	data = serializers.serialize("xml", AreaProduccion.objects.all())
	return HttpResponse(data, content_type="application/xml")