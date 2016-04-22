from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/$', views.myPost, name='myPost'),
    url(r'^post/$', views.post, name='post'),
    url(r'^yourPost/$', views.yourPost, name='yourPost'),

]
