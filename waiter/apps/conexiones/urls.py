from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.conexiones', 	
	url(r'^configurations/$', 'views.view_configuration_products',name = 'vista_configuracion_productos'),		
	url(r'^test_conexion/$', 'rest.test_conexion',name = 'vista_test_conexion'),

)