from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^authen/$', views.authen, name='authen'),
    url(r'^index/$', views.index, name='index'),
]