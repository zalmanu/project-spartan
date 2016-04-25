from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/', views.register_page, name='register'),
    url(r'^login/', views.login_page, name='login'),
    url(r'^reset/', views.reset_pass, name='reset'),
    url(r'^forgot/','django.contrib.auth.views.password_reset',{'template_name': 'authentication/forget.html'}, name='reset_password_reset1'),
    url(r'^forgot/done/', 'django.contrib.auth.views.password_reset_done',{ 'extra_context': {'confirms': ['We sent you an email']}}, name='password_reset_done'),
    url(r'^newpass/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',{'template_name': 'authentication/newpass.html'}, name='password_reset_confirm'),
    url(r'^newpass/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete')
]
