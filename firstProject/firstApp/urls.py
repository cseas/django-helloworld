from django.urls import path
from django.conf.urls import url
from firstApp import views

app_name = 'firstApp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
]