from django.conf.urls import patterns, url

from questions import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topic_id>\d+)/$', views.detail, name='detail'),
    url(r'^finish/$', views.finish, name='finish'),
    url(r'^createuser/$', views.create_user, name='createuser'),
    url(r'^login/$', views.authenticate_user, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^(?P<topic_id>\d+)/verify/$', views.verify, name='verify'),
    url(r'^(?P<topic_id>\d+)/update/$', views.update, name='update'),

)