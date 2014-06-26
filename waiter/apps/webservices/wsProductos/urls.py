from django.conf.urls import patterns, url

urlpatterns = patterns('waiter.apps.webservices.wsProductos.views',
	url(r'^ws/products/json$', 'ws_Products_view_js',name = 'ws_products_url_js'),
	url(r'^ws/products/xml$', 'ws_Products_view_xml',name = 'ws_products_url_xml'),
	url(r'^ws/categories/json$', 'ws_Categories_view_js',name = 'ws_categories_url_js'),
	url(r'^ws/categories/xml$', 'ws_Categories_view_xml',name = 'ws_categories_url_xml'),
	url(r'^ws/areas/jsonp$', 'ws_AreaProduccion_view_js',name = 'ws_areas_url_js'),
	url(r'^ws/areas/xml$', 'ws_AreaProduccion_view_xml',name = 'ws_areas_url_xml'),
)