from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^faq/$', views.faq, name='faq'),

]
