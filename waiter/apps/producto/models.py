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
	categoria = models.ForeignKey(Categoria)
	#categoria = models.OneToOneField(Categoria)
	areaProduccion = models.ForeignKey(AreaProduccion)
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

class DetalleIngrediente(models.Model):
	nombre = models.CharField(max_length=200, help_text='Componente de ingrediente específico.')
	ingrediente = models.ForeignKey(Ingrediente)
	class Meta:
		db_table = ('DetalleIngrediente')
		verbose_name = ('Detalle de ingrediente')
		verbose_name_plural = ('Detalle de ingredientes')
	def __unicode__(self):
		return self.nombre

class Composicion(models.Model):
	cantidad = models.IntegerField(help_text='Detalla la cantidad de ingredientes a utilizar.')
	visible = models.BooleanField(default=True, help_text='Active la opcion para que la composición este activa.')
	ingrediente = models.ForeignKey(Ingrediente)
	producto = models.ForeignKey(Producto)

	class Meta:
		db_table = ('Composicion')
		verbose_name = ('Composición')
		verbose_name_plural = ('Composiciones')
	def __unicode__(self):
		return '%s %s' % (self.cantidad, self.ingrediente.nombre)    
    
    #Codigo Jairo
class GrupoIngrediente(models.Model):
	nombre = models.CharField(max_length=200, help_text='Componente de ingrediente específico.')
	detallePreparacion = models.CharField(mas_length=200, help_text='detallePreparacion')
	modificable= models.BooleanField(default=,help_text='Active esta opcion para que este activa')
     class Meta:
     	db_table = ('GrupoIngrediente')
     	verbose_name =('GrupoIngrediente')
     	verbose_name_plural = ('GrupoIngredientes')
    def __unicode__(self):
        return '%s %s' % (self.nombre, self.detallePreparacion)

class Composicion_GrupoIngrediente(models.Model):
	composicion = models.Composicion
	grupoingrediente= models.GrupoIngrediente

    class Meta:
       ss Meta:
     	db_table = ('Composicion_GrupoIngrediente')
     	verbose_name =('Composicion_GrupoIngrediente')
     	verbose_name_plural = ('Composicion_GrupoIngredientes')

    def __unicode__(self):
        return '%s %s' % (self.composicion, self.grupoingrediente)
    )

class Grupoingrediente_Ingrediente(models.Model):
          verbose_name = _('MODELNAME')
        verbose_name_plural = _('MODELNAMEs')

    def __unicode__(self):
        pass
    


	


		


		
		
