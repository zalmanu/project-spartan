from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^review/$', views.review, name='review')

 ]