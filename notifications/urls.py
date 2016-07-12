from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^seen/$', views.seen, name='seen')
]
