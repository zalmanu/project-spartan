from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^submit/', views.create_post, name='submit'),
    url(r'^gradina/', views.garden, name='garden'),
    url(r'^transport/', views.transport, name='transport'),
    url(r'^curatenie/', views.curatenie, name='curatenie'),
    url(r'^baby/', views.baby, name='baby'),
    url(r'^gatit/', views.gatit, name='gatit'),
    url(r'^altele/', views.altele, name='altele'),
    url(r'^profile/', views.profile, name='profile')
]
