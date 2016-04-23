from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/', views.register_page, name='register'),
    url(r'^login/', views.login_page, name='login'),
    url(r'^reset/', views.reset_pass, name='reset'),
    url(r'^forgotpassword/', views.forgotpassword, name='forgotpassword'),
    url(r'^forgotpassword/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
            views.reset_confirm, name='password_reset_confirm')
]
