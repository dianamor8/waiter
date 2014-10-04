# -*- coding: utf-8 -*-
import MySQLdb
import psycopg2
from waiter.settings import LOGIN_URL, LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
import json


05
@login_required(login_url=LOGIN_URL)
def test_conexion(request):	
	# Establecemos la conexion con la base de datos	 
	# MEJOR CONEXION CON CONECTOR
	# >>>>>>>>>>>>>>>>>>>>>>>>>>>
	# http://www.slideshare.net/BaabtraMentoringPartner/database-connectivity-in-python
	# >>>>>>>>>>>>>>>>>>>>>>>>>>>
	# http://initd.org/psycopg/docs/connection.html
	# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
	# 
	if request.is_ajax():		
		if request.method == 'POST':
			fuente = request.POST.get('fuente')	
			gestor = request.POST.get('gestor')	
			database = request.POST.get('database')	
			userdb = request.POST.get('userdb')	
			passworddb = request.POST.get('passworddb')	
			host = request.POST.get('host')	
			port = request.POST.get('port')		

			if gestor == '0':
				print "entra en 0"
				try:
					bd = MySQLdb.connect(host=host,user=userdb,password=passworddb,database=database, port=port)
					print "si conecta con mysql"					
					ctx={'respuesta':'si conecta'}
					return HttpResponse(json.dumps(ctx), content_type='application/json')	
				except Exception, e:				
					print "no conecta con mysql"
					ctx={'respuesta':'no conecta'}
					return HttpResponse(json.dumps(ctx), content_type='application/json')	
					raise e
			if gestor == '1':
				print "entra en 1"
				try:
					bd = psycopg2.connect(host=host,user=userdb,password=passworddb,database=database, port=port)
					print "si conecta con postgresql"
					ctx={'respuesta':'si conecta'}
					return HttpResponse(json.dumps(ctx), content_type='application/json')	
				except Exception, e:				
					print "no conecta con postgresql"
					ctx={'respuesta':'no conecta'}
					return HttpResponse(json.dumps(ctx), content_type='application/json')	
					raise e



			

			# errores = form_categorie.errors
			
			
# >> algun metodo de conexion
			# http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
			

			# http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
			# http://www.micahcarrick.com/ajax-form-submission-django.html
			# https://docs.djangoproject.com/en/1.6/ref/contrib/csrf/
			# http://stackoverflow.com/questions/7335780/how-to-post-a-django-form-with-ajax-jquery
			# http://stackoverflow.com/questions/5304517/ajax-post-in-django-framework
			# http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
		#else:
			# bd = MySQLdb.connect("localhost","usuariojiji","prueba123","prueba_db" )
			# # Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de dato
			# cursor = bd.cursor()
			# # Ejecutamos un query SQL usando el metodo execute() que nos proporciona el cursor
			# cursor.execute("SELECT VERSION()")
			# # Extraemos una sola fila usando el metodo fetchone()
			# data = cursor.fetchone()
			# print "Versión Base de Datos : %s " % data 
			# # Nos desconectamos de la base de datos
			# bd.close()