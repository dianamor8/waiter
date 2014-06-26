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
	print "entraa ajax"
	if request.is_ajax():
		if request.method == 'POST':
			respuesta = False
			form_categorie = addCategoriaForm(request.POST)
			if form_categorie.is_valid():
				form_categorie.save()
				respuesta = True
				categorias = Categoria.objects.all()
				lista = list()
				for categoria in categorias:
					lista.append({'tabla':'<tr><td> %s</td><td> %s</td> <td> <a data-target="#categorieModal" class="btn btn-default btn-xs call" data-toggle="modal" data-id="%s"> <span class="glyphicon glyphicon-pencil"></span> Actualizar </a> </td></tr>'%(categoria.id,categoria.nombre, categoria.id)})
				ctx={'respuesta':respuesta, 'tabla':lista}		
		return HttpResponse(json.dumps(ctx), content_type='application/json')	
	else:
		Http404

		