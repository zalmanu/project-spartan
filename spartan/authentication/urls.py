# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/', views.register_page, name='register'),
    url(r'^login/', views.login_page, name='login'),
    url(r'^reset/', views.reset_pass, name='reset'),
    url(r'^forgot/', 'django.contrib.auth.views.password_reset',
        {'template_name': 'authentication/forget.html'},
        name='reset_password_reset1'),
    url(r'^forgot/done/', 'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),
    url(r'^newpass/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'authentication/newpass.html'},
        name='password_reset_confirm'),
    url(r'^newpass/done/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'authentication/new_done.html'},
        name='password_reset_complete')
]
