from django.conf.urls import patterns, url
from django.conf import settings
from trends import views


urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
  	
    url(r'^tendencias/(?P<ident>.*)/$', views.detalle, name='detalle'),
	url(r'^resumen/(?P<identrs>.*)/$', views.resumen, name='resumen'),

	url(r'^media/(?P<path>.*)$','django.views.templates.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	url(r'informacion/', views.information, name='information'),

	



)