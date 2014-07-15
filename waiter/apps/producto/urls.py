# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.producto',
	url(r'^products$', 'views.products_view',name = 'vista_products'),
	url(r'^add/product/$', 'views.add_product_view',name = 'vista_add_product'),	
	
	#CATEGORIA 
	url(r'^add/new/categorie/$', 'rest.add_categorie_ajax',name = 'vista_add_new_categorie'),
	url(r'^update/categorie/$', 'rest.update_categorie_ajax',name = 'vista_update_categorie'),
	url(r'^delete/categorie/$', 'rest.delete_categorie_ajax',name = 'vista_delete_categorie'),
	url(r'^categories/$', 'views.categories_view',name = 'vista_categories'),
	# Con o sin parámetro
	url(r'^categoriesproducts/(?:(?P<id_categorie>\d+)/)?$', 'views.categories_product_view',name = 'vista_categories_products'),
	
	# AREA DE PRODUCCIÓN
	url(r'^areas/$', 'views.areas_de_produccion_view',name = 'vista_areas_produccion'),
	url(r'^new/area/$', 'rest.add_area_ajax',name = 'vista_add_new_area'),
	url(r'^update/area/$', 'rest.update_area_ajax',name = 'vista_update_area'),
	url(r'^delete/area/$', 'rest.delete_area_ajax',name = 'vista_delete_area'),	
)

