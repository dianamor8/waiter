from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.home.views', 
	url(r'^$', 'index_view',name = 'vista_principal'),
	url(r'^about/$', 'about_view',name = 'vista_about'),
	url(r'^contact/$', 'contact_view',name = 'vista_contacto'),
	url(r'^login/$', 'login_view',name = 'vista_login'),
	url(r'^logout/$', 'logout_view',name = 'vista_logout'),
)

