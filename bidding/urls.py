from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/$', views.posts, name='myPost'),
    url(r'^post/(?P<slug>[^\.]+)/$', views.post, name='post'),
    url(r'^yourPost/$', views.yourPost, name='yourPost'),

]
