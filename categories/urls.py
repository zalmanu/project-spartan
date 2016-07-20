from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^category/(?P<kind>\w+)/$', views.category, name='category'),
    url(r'^filter/$', views.filter, name='filter')
]
