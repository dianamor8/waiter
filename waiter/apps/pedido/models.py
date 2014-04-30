# -*- coding: utf-8 -*-
from django.db import models
from waiter.apps.producto.models import Producto

# Create your models here.

PEDIDO = 0
PREPARANDO = 1
DESPACHADO = 2
ESTADO_CHOICES = (
	(PEDIDO, 'PEDIDO'),
	(PREPARANDO, 'PREPARANDO'),
	(DESPACHADO, 'DESPACHADO'),
)

class Pedido(models.Model):
	codigo = models.BigIntegerField(help_text='Código de Pedido', unique=True)
	fecha = models.DateField()
	mesa = models.IntegerField(help_text='Numero de Mesa')
	estado_pedido = models.CharField(choices=ESTADO_CHOICES,max_length=2)
	
	class Meta:
		db_table = ('Pedido') #atribute to change name on database table 
		verbose_name = ('Pedido')
		verbose_name_plural = ('Pedidos')

		
	def __unicode__(self):
		return self.codigo


class ItemPedido(models.Model):
	cantidad = models.IntegerField(help_text='Cantidad de Pedidos')
	producto = models.ForeignKey(Producto)
	pedido = models.ForeignKey(Pedido)
	despachandose = models.BooleanField(default=False)
	#composionPedido = models.ManyToManyField()

	class Meta:
		db_table = ('ItemPedido')
		verbose_name = ('Item Pedido')
		verbose_name_plural = ('Item Pedidos')

	def __unicode__(self):
		pass



