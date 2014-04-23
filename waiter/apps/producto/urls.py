from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.producto.views',
	url(r'^productos/$', 'productos_view',name = 'vista_productos'),
	url(r'^add/product/$', 'add_product_view',name = 'vista_add_product'),	
)