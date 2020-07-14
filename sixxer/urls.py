from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^oauth/', include('social_django.urls', namespace='social')),
                  url('^auth/', include(('django.contrib.auth.urls', 'auth'), namespace='auth')),
                  url('', include('sixerapp.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

