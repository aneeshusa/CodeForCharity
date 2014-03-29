from django.conf.urls import patterns, url

from questions import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topic_id>\d+)/$', views.detail, name='detail'),
    url(r'^finish/$', views.finish, name='finish'),
)