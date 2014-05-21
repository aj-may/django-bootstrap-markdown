from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'test_app.views.test_view'),
    url(r'^markdown/', include('django_bootstrap_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
