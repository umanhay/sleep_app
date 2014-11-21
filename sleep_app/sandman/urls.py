from django.conf import settings
from django.conf.urls import patterns, url
from sandman import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^help/$', views.help, name='help'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )