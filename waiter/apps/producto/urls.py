from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.producto.views',
	url(r'^products$', 'products_view',name = 'vista_products'),
	url(r'^add/product/$', 'add_product_view',name = 'vista_add_product'),	
	url(r'^add/categorie/$', 'add_categorie_view',name = 'vista_add_categorie'),
	url(r'^categories/$', 'categories_view',name = 'vista_categories'),
	url(r'^areas/$', 'areas_de_produccion_view',name = 'vista_areas_produccion'),
)