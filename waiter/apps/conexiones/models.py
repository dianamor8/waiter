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
	descripcion = models.CharField(max_length=100)
	class Meta:		
		db_table = ('Conexion')
		verbose_name= ('Conexión')		
		verbose_name_plural= ('Conexiones')		
	def __unicode__(self):
		return self.fuente


class DatosConexion(models.Model):	
	conexion = models.ForeignKey(Conexion)
	nombre_parametro = models.CharField(max_length=200) 
	valor_parametro = models.CharField(max_length=200) 
	class Meta:
		ordering = ['nombre_parametro']
		db_table = ('DatosConexion')
		verbose_name= ('Dato de conexión')		
		verbose_name_plural = ('Datos de conexión')	
	def __unicode__(self):
		return '%s : %s'%(self.nombre_parametro, self.valor_parametro)
