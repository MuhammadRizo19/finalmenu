from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('baseapp.urls')),
    path('rosetta/', include('rosetta.urls')),
)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "O\'rda Restaurant"
admin.site.site_title = "O\'rda CRM"