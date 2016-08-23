from django.conf.urls import url

from . import views

app_name = 'blogs'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.tags, name='tags'),
]