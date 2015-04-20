from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'supermarket.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
	url(r'^app/', include('iSupermarket.urls', namespace='iSupermarket')),
	url(r'^admin/', include(admin.site.urls)),
)