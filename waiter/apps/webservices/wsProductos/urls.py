from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.webservices.wsProductos.views',
	url(r'^ws/products$', 'ws_Products_view',name = 'ws_products_url'),
)