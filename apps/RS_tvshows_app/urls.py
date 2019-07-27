from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^shows$',views.shows),
    url(r'^shows/new$',views.new_shows),
    url(r'^shows/create$',views.process_create),
    url(r'^shows/(?P<show_id>\d+)$',views.read_shows),
    url(r'^shows/(?P<show_id>\d+)/edit$',views.update_shows),
    url(r'^shows/(?P<show_id>\d+)/update$',views.process_update),
    url(r'^shows/(?P<show_id>\d+)/destroy$',views.process_destroy),
]