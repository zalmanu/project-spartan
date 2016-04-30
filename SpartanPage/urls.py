from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/$', views.user, name='user'),

]
