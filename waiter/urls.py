from django.conf.urls import patterns, include, url
from waiter import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waiter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^', include('waiter.apps.home.urls')),
	url(r'^', include('waiter.apps.producto.urls')),	
	url(r'^admin/', include(admin.site.urls)),	
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),	
)