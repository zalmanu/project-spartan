from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^chat/(?P<slug>[^\.]+)/$', views.room, name='room'),
    url(r'^rooms/$', views.rooms, name='rooms')
]
