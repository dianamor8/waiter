from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.home.views', 
	url(r'^$', 'index_view',name = 'vista_principal'),
	url(r'^about/$', 'about_view',name = 'vista_about'),	
)

