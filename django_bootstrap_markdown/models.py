from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import Transpose, ResizeToFit, SmartResize


class Image(models.Model):
    original = models.ImageField(
        upload_to='markdown/images/',
        verbose_name=_(u'Original Image')
    )
    large = ImageSpecField(
        source='original',
        processors=[Transpose(), ResizeToFit(750, 400, upscale=False)],
        options={'quality': 85},
        verbose_name=_(u'Large Image')
    )
    medium = ImageSpecField(
        source='original',
        processors=[Transpose(), ResizeToFit(375, 400, upscale=False)],
        options={'quality': 85},
        verbose_name=_(u'Medium Image')
    )
    small = ImageSpecField(
        source='original',
        processors=[Transpose(), ResizeToFit(185, 400, upscale=False)],
        options={'quality': 85},
        verbose_name=_(u'Small Image')
    )
    billboard = ImageSpecField(
        source='original',
        processors=[Transpose(), SmartResize(750, 300)],
        options={'quality': 85},
        verbose_name=_(u'Billboard Image')
    )
    description = models.CharField(
        max_length=200,
        verbose_name=_(u'Description')
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'Timestamp')
    )

    class Meta:
        ordering = ['-timestamp']
        verbose_name = _(u'image')
        verbose_name_plural = _(u'images')
        app_label = _(u'Django Bootstrap Markdown')
