from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django_markdown_project.views.test'),
    url(r'^markdown/', include('django_bootstrap_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.MEDIA_URL == '/media/':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)