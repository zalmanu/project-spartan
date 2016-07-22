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

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('authentication.urls')),
    url(r'^', include('homepages.urls')),
    url(r'^', include('posts.urls')),
    url(r'^', include('bidding.urls')),
    url(r'^', include('contact_us.urls')),
    url(r'^', include('chat.urls')),
    url(r'^', include('categories.urls')),
    url(r'^', include('spartans.urls')),
    url(r'^', include('profiles.urls')),
    url(r'^', include('review.urls')),
    url(r'^', include('report.urls')),
    url(r'^', include('notifications.urls'))



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    url(r'^faq/$', TemplateView.as_view(template_name="faq/faq.html")),
    url(r'^about/$', TemplateView.as_view(
        template_name="about_us/about_us.html")),
]


handler404 = 'errorPages.views.handler404'
handler500 = 'errorPages.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
