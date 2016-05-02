from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^spartan/$', views.spartan, name='spartan'),
    url(r'^user/$', views.user, name='userSpartan'),
    url(r'^user/(?P<slug>[^\.]+)/$', views.user, name='SpartanUser')
]

handler404 = 'views.custom_404'
handler404 = 'views.custom_500'