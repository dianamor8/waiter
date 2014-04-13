from django.contrib import admin
from waiter.apps.producto.models import Categoria, AreaProduccion, Operacion, Producto, Composicion, Ingrediente, DetalleIngrediente
# Register your models here.

class OperacionAdmin(admin.TabularInline):
	model = Operacion
	extra = 1


class ComposicionAdmin(admin.TabularInline):
	model = Composicion
	extra = 1

class DetalleIngredienteAdmin(admin.TabularInline):
	model = DetalleIngrediente
	extra = 1			

class ProductoAdmin(admin.ModelAdmin):
	inlines = [OperacionAdmin, ComposicionAdmin]

class IngredienteAdmin(admin.ModelAdmin):
	inlines = [DetalleIngredienteAdmin]


	
admin.site.register(Categoria)
admin.site.register(AreaProduccion)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Producto, ProductoAdmin)
