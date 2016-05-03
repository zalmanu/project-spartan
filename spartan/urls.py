from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^spartan/$', views.spartan, name='spartan'),
    url(r'^user/$', views.user, name='userSpartan'),
    url(r'^user/(?P<slug>[^\.]+)/$', views.user, name='SpartanUser')
]

