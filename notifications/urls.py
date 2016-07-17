from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^seen/$', views.seen, name='seen'),
    url(r'^delete/$', views.notification_delete, name='delete')
]
