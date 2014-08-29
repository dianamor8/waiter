# -*- coding: utf-8 -*-
from django.db import models

class Product_external_view(models.Model):	
	nombre = models.CharField(max_length=300)
	precio = models.DecimalField(decimal_places=2)
	class Meta:
		app_label = 'productoexterno'
		db_table = ('Product_external_view')
	def __unicode__(self):
		return "[%s - %s]"%(self.nombre,self.precio)

CONEXION_LOCAL = 0	
CONEXION_EXTERNA = 1
CONEXION_WEB_SERVICE = 2
CONEXION_CHOICES = (
	(CONEXION_LOCAL, 'Conexión Local'),
	(CONEXION_EXTERNA, 'Conexión con una base de datos externa'),
	(CONEXION_WEB_SERVICE, 'Conexión con servicios web'),
)


ACTIVO = 1	
NO_ACTIVO = 0
ESTADO_CHOICES = (
	(ACTIVO, 'ACTIVO'),
	(NO_ACTIVO, 'NO ACTIVO'),
)

class Conexion(models.Model):	
	fuente = models.CharField(choices=CONEXION_CHOICES, max_length=2, unique=True)
	estado = models.CharField(choices=ESTADO_CHOICES, max_length=2)
	configurado = models.BooleanField(default=False)
	class Meta:		
		db_table = ('Conexion')
		verbose_name= ('Conexión')		
		verbose_name_plural= ('Conexiones')		
	def __unicode__(self):
		return self.fuente

MYSQL = 0	
POSTGRESQL = 1
BASES_CHOICES = (
	(MYSQL, 'MYSQL'),
	(POSTGRESQL, 'POSTGRESQL'),
)

class ConexionDB(models.Model):	
	gestor = models.CharField(choices=BASES_CHOICES, max_length=50)
	database = models.CharField(max_length=50,help_text='Nombre de la base de datos.')
	userdb = models.CharField(max_length=50, help_text='Nombre de usuario.')
	passworddb = models.CharField(max_length=50, help_text='Contraseña de acceso.')
	host = models.IPAddressField(help_text='Dirección host del equipo.', unique=True)	
	port = models.CharField(max_length=50, help_text='Puerto de conexión.')
	class Meta:		
		db_table = ('ConexionDB')
		verbose_name= ('Conexion con base de datos.')		
		verbose_name_plural = ('Conexiones con base de datos.')	
	def __unicode__(self):
		return '%s : %s'%(self.gestor, self.database)