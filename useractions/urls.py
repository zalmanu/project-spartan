from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^submit/$', views.create_post, name='submit'),
    url(r'^category/(?P<kind>[^/]+)/$', views.category, name='category'),
    url(r'^profile/$', views.profile, name='profile')
]
