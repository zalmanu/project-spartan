from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout/', views.logout_view, name='logout')
]