from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^about/', views.about, name='about'),
    url(r'^$', views.index, name='index')
)
