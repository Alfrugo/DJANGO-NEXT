

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.urls import include, path
from api.views import home  # import your view



urlpatterns = [
    path('', home, name='home'),  # add a URL pattern for the root
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
]

# This is only for development! In production, use a web server to serve media files.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
