from django.conf.urls import url
from . import views          
  
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),  
    url(r'^destroy/(?P<id>\d+)$', views.delete),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
]