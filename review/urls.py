from django.conf.urls import url
from . import views

urlpatterns = [

 url(r'^review/(?P<slug>[^\.]+)/(?P<url_hash>\w+)/$', views.review, name='review')
 ]
