from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^room/(?P<slug>[^\.]+)/$', views.room, name='room'),
    url(r'^mail/$', views.rooms, name='rooms')
]
