from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.producto',
	url(r'^products$', 'views.products_view',name = 'vista_products'),
	url(r'^add/product/$', 'views.add_product_view',name = 'vista_add_product'),	
	url(r'^add/categorie/$', 'views.add_categorie_view',name = 'vista_add_categorie'),
	url(r'^add/new/categorie/$', 'rest.add_categorie_ajax',name = 'vista_add_new_categorie'),
	url(r'^categories/$', 'views.categories_view',name = 'vista_categories'),
	url(r'^areas/$', 'views.areas_de_produccion_view',name = 'vista_areas_produccion'),
)