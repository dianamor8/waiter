from django.contrib import admin
from waiter.apps.producto.models import *
from waiter.apps.pedido.models import *
from waiter.apps.conexiones.models import *
# Register your models here.

class ComposicionAdmin(admin.TabularInline):
	model = Composicion
	extra = 1

class ProductoAdmin(admin.ModelAdmin):
	inlines = [ComposicionAdmin]

admin.site.register(Categoria)
admin.site.register(AreaProduccion)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Composicion)
admin.site.register(Ingrediente)
admin.site.register(GrupoIngrediente)
admin.site.register(Pedido)
admin.site.register(Conexion)
admin.site.register(ConexionDB)