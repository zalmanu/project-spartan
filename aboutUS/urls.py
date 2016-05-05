from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^aboutus/$', views.aboutUS, name='contact'),

]
