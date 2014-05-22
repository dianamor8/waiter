from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.usuarios.views', 
	#url(r'^login/$', 'login_view',name = 'vista_login'),	
	url(r'^login/$', 'forms_view',name = 'vista_login'),	
	url(r'^logout/$', 'logout_view',name = 'vista_logout'),	
)

# modificar 2 modelos http://django.es/blog/utilizar-un-formulario-para-modificar-2-modelos/
