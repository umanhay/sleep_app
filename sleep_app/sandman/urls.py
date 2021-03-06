from django.conf.urls import patterns, url
from sandman import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^ajax/$', views.ajax, name='ajax'),
        url(r'^dom/$', views.dom, name='dom'),
        url(r'^help/$', views.help, name='help'),
        url(r'^charmed/$', views.charmed, name='charmed'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login, name='login'),
        url(r'^help_ajax/$', views.help_ajax, name='help_ajax'),
)

