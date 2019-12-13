from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

admin.site.site_header = 'KBA Website Admin'
admin.site.site_title = 'KBA Website Admin'

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('events', include('events.urls')),
    path('boardmembers', include('boardmembers.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('alumni/', include('alumni.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)