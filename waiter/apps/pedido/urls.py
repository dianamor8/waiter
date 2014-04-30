from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.pedido.views',
	url(r'^order$', 'pedido_view',name = 'vista_order'),
	)