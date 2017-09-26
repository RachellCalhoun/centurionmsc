from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog$', views.post_list, name='post_list'),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.event_detail, name='event_detail'),
     url(r'^events/$', views.event_calendar, name='event_calendar'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]