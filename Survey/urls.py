from django.conf.urls import include,url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^survey/', views.survey ,name='survey'),
    url(r'^results/$', views.vote, name='vote'),

]