"""
这是users的urls
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/', login , {'template_name': 'users/login.html'}, name='login'),
    url(r'log_out/$', views.log_out, name='log_out'),
    #url(r'zhuxiao', views.log_out, name='zhuxiao'),
]
