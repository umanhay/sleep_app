from django.conf.urls import patterns, url
from sandman import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^ajax/$', views.ajax, name='ajax'),
        url(r'^help/$', views.help, name='help'),
        url(r'^charmed/$', views.charmed, name='charmed'),
        url(r'^settings/$', views.settings, name='settings'),
)

