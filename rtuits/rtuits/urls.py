from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rtuits.views.home', name='home'),
    # url(r'^rtuits/', include('rtuits.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^',include('trends.urls')),
    url(r'^tendencias/', include('trends.urls')),
    url(r'^resumen/$', include('trends.urls')),
    url(r'^resumen/(.*)/$', include('trends.urls')),
    url(r'^informacion/', include('trends.urls')),
    url(r'^admin/', include(admin.site.urls)),




    

)


