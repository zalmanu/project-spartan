from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^general/$', views.profileGeneral, name='profilGeneral')
]
