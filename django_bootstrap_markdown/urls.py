from django.conf.urls import patterns, include, url

urlpatterns = patterns('django_bootstrap_markdown.views',
    url(r'^image/$', 'markdown_image'),
    url(r'^image/library/$', 'markdown_library'),
)
