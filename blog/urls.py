from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/$', views.post, name='post'),
    url(r'^$', views.index, name='index'),
]
