# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)	
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
		verbose_name_plural = ('Áreas de Producción')

	def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	codigo = models.CharField(max_length=100, help_text='Código de producto', unique=True)
	nombre = models.CharField(max_length=300, help_text='Ingrese el nombre del producto')
	precio = models.DecimalField(max_digits=7, decimal_places=2, help_text='Registre el precio de del producto.')
	#imagen = models.ImageField(help_text='Seleccione una imagen.')
	estado = models.BooleanField(default=True,  help_text='Seleccione la opción para que el producto se mantenga activo.')
	categoria = models.OneToOneField(Categoria)
	areaProduccion = models.OneToOneField(AreaProduccion)
	class Meta:
		ordering = ['nombre']
		db_table = ('Producto')
		verbose_name= ('Producto')		
		verbose_name_plural = ('Productos')		

	def __unicode__(self):
		return self.nombre
    
    


class Operacion(models.Model):
	modificable = models.BooleanField(default=True, help_text='Seleccione esta opción si este producto puede editarse')
	tiempoActualizacion = models.IntegerField(help_text='Ingrese el tiempo máximo que un cliente puede modificar su pedido')
	producto = models.OneToOneField(Producto)
	class Meta:
		db_table = ('Operacion')
		verbose_name = ('Operación')
		verbose_name_plural = ('Operaciones')
	def __unicode__(self):	
		return '[%s : %s - %s min]' % (self.producto.nombre, self.modificable, self.tiempoActualizacion)
    