from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^spartan/$', views.spartan, name='spartan')
]
