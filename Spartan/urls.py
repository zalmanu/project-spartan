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
    url(r'^', include('contact_us.urls')),
    url(r'^', include('chat.urls')),
    url(r'^', include('categories.urls')),
    url(r'^', include('spartans.urls')),
    url(r'^', include('profiles.urls')),
    url(r'^', include('review.urls')),
    url(r'^', include('faq.urls')),
    url(r'^', include('report.urls')),
    url(r'^', include('about_us.urls')),
    url(r'^', include('notifications.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'errorPages.views.handler404'
handler500 = 'errorPages.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
