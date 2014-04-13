from django.contrib import admin
from waiter.apps.producto.models import Categoria, AreaProduccion, Operacion, Producto
# Register your models here.

class OperacionAdmin(admin.TabularInline):
	model = Operacion
	extra = 0

class ProductoAdmin(admin.ModelAdmin):
	inlines = [OperacionAdmin]

	
admin.site.register(Categoria)
admin.site.register(AreaProduccion)
admin.site.register(Operacion)
admin.site.register(Producto, ProductoAdmin)
