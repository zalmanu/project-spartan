from django.conf.urls import url
from . import views

urlpatterns = [

 url(r'^review/(?P<slug>[^\.]+)/$', views.review, name='review')


 ]