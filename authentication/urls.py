from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/', views.register_page, name='register'),
    url(r'^login/', views.login_page, name='login'),
    url(r'^reset/', views.reset_pass, name='reset'),
    # url(r'^forGotPassword/', views.forgot, name='forgot'),
    # url(r'^newpass/', views.forgotnewpass, name='newpass'),
    url(r'^forGotPassword/','django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    url(r'^forGotPassword/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^newpass/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^newpass/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete')
]