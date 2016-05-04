"""Spartan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add   a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('authentication.urls')),
    url(r'^', include('homepages.urls')),
    url(r'^', include('posts.urls')),
    url(r'^', include('bidding.urls')),
    url(r'^', include('contactUS.urls')),
    url(r'^', include('chat.urls')),
    url(r'^', include('categories.urls')),
    url(r'^', include('spartan.urls')),
    url(r'^', include('profiles.urls')),
    url(r'^', include('review.urls')),
    url(r'^', include('faq.urls')),
    url(r'^', include('report.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'errorPages.views.handler404'
handler500 = 'errorPages.views.handler500'
