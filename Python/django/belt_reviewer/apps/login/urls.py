from django.conf.urls import url
from . import views          
  
urlpatterns = [
    url(r'^$', views.index),
    url(r'process$', views.process),   
    url(r'books$', views.success), 
    url(r'login$', views.login),   
    url(r'add$', views.add), 
]