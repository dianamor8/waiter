# -*- coding: utf-8 -*-
from django.shortcuts import render
from waiter.apps.conexiones.models import Product_external_view
from waiter.settings import LOGIN_URL, LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from waiter.apps.conexiones.forms import addConexionDataBaseForm, TypeConexionForm, ConexionDBForm
import MySQLdb
# Create your views here.

@login_required(login_url=LOGIN_URL)
def view_configuration_productos(request):
	productos = Product_external_view.objects.all()	
	if request.method=='GET':		
		form = addConexionDataBaseForm()		
		ctx = {'productos':productos, 'sidebar':'administracion', 'form_conexion':form}
	else:	
		ctx = {'productos':productos, 'sidebar':'administracion'}
	return render(request, 'home/panel_administracion/configurations.html', ctx)


@login_required(login_url=LOGIN_URL)
def view_configuration_products(request):
	if request.method=='GET':		
		# ctx = {'holi':'holi'}
		
		# bd = MySQLdb.connect("localhost","usuarioprueba","prueba123","prueba_db" )
		# # Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de dato
		# cursor = bd.cursor()
		# # Ejecutamos un query SQL usando el metodo execute() que nos proporciona el cursor
		# cursor.execute("SELECT VERSION()")
		# # Extraemos una sola fila usando el metodo fetchone()
		# data = cursor.fetchone()
		# print "Versión Base de Datos : %s " % data 
		# # Nos desconectamos de la base de datos
		# bd.close()
	# else:
		form_type_conexion = TypeConexionForm()
		form_conexion = ConexionDBForm()
		ctx = {'form_type_conexion':form_type_conexion, 'form_conexion': form_conexion, 'sidebar':'administracion'}
		print "pasando por la viewwwwww >>>>>"
		return render(request, 'home/panel_administracion/configuraciones.html', ctx)

