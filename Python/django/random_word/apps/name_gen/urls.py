from django.conf.urls import url
from . import views           # This line is new!
  
  
urlpatterns = [
    url(r'^$', views.index),     # This line has changed! views.index points to views methods file 
    url(r'^generate$', views.generate),
    url(r'^reset', views.reset)
]