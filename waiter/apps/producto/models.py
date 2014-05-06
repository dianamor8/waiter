# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length=200, help_text='Agrege el nombre de la categoría')	
	class Meta:
		db_table = ('Categoria')
		verbose_name = ('Categoría')
		verbose_name_plural = ('Categorías')
	def __unicode__(self):
		return self.nombre

class AreaProduccion(models.Model):
	nombre = models.CharField(max_length=200, help_text='Ingrese el nombre del área de producción.')
	class Meta:
		db_table = ('AreaProduccion') #atribute to change name on database table 
		verbose_name = ('Área de producción')
		verbose_name_plural = ('Áreas de producción')

	def __unicode__(self):
		return self.nombre

#Tipo enumerado para el estado del producto
ACTIVO = 1	
NO_ACTIVO = 0
ESTADO_CHOICES = (
	(ACTIVO, 'ACTIVO'),
	(NO_ACTIVO, 'NO ACTIVO'),
)

class Producto(models.Model):

	codigo = models.CharField(max_length=100, help_text='Código de producto', unique=True)
	nombre = models.CharField(max_length=300, help_text='Ingrese el nombre del producto')
	precio = models.DecimalField(max_digits=7, decimal_places=2, help_text='Registre el precio de del producto.')
	#imagen = models.ImageField(help_text='Seleccione una imagen.')	
	categoria = models.ForeignKey(Categoria)	
	areaProduccion = models.ForeignKey(AreaProduccion)
	estado = models.CharField(choices=ESTADO_CHOICES, max_length=30)
	class Meta:
		ordering = ['nombre']
		db_table = ('Producto')
		verbose_name= ('Producto')		
		verbose_name_plural = ('Productos')	
	def __unicode__(self):
		return self.nombre

class Ingrediente(models.Model):
	nombre = models.CharField(max_length=200, help_text='Ingrese el nombre del ingrediente.')
	tiempoPreparacion = models.IntegerField(help_text='Registre el tiempo de preparación de este ingrediente')
	detallePreparacion = models.TextField(help_text='Registre un detalle de preparación del ingrediente.')	
	class Meta:
		db_table = ('Ingrediente')
		verbose_name = ('Ingrediente')
		verbose_name_plural = ('Ingredientes')
	def __unicode__(self):
		return '%s : %s min' % (self.nombre, self.tiempoPreparacion)

#Codigo Jairo
class GrupoIngrediente(models.Model):
	nombre = models.CharField(max_length=200, help_text='Registre el d del grupo de ingredientes.')
	detallePreparacion = models.TextField(help_text='Agregue detalles de preparación del grupo.')
	modificable= models.BooleanField(default=True, help_text='Active esta opcion si éste componente es editable')	
	ingredientes = models.ManyToManyField(Ingrediente)
	
	class Meta:
		db_table = ('GrupoIngrediente')
		verbose_name =('GrupoIngrediente')
		verbose_name_plural = ('GrupoIngredientes')
		def __unicode__(self):
			return '%s %s' % (self.nombre, self.detallePreparacion)

class Composicion(models.Model):
	cantidad = models.IntegerField(help_text='Detalla la cantidad de ingredientes a utilizar.')
	visible = models.BooleanField(default=True, help_text='Active la opcion para que la composición este activa.')
	producto = models.ForeignKey(Producto)
	gruposIngredientes = models.ManyToManyField(GrupoIngrediente)
	ingredientes = models.ManyToManyField(Ingrediente)
	class Meta:
		db_table = ('Composicion')
		verbose_name = ('Composición')
		verbose_name_plural = ('Composiciones')
	def __unicode__(self):
		return '%s %s' % (self.cantidad, self.producto.nombre) 