from django.contrib import admin
from imagekit.admin import AdminThumbnail
from django_bootstrap_markdown.models import Image


class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ('admin_thumbnail', 'original', 'description')
    list_display_links = ['original']
    admin_thumbnail = AdminThumbnail(image_field='small')

admin.site.register(Image, ImageAdmin)
