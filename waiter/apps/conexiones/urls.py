from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.conexiones.views', 	
	url(r'^configurations/$', 'view_configuration_productos',name = 'vista_configuracion_productos'),		
)