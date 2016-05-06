from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/$', views.create_post, name='submit'),
    url(r'^post/(?P<slug>[^\.]+)/$', views.post, name='post'),
    url(r'^edit/(?P<slug>[^\.]+)/$', views.edit_post, name='edit_post')
]
