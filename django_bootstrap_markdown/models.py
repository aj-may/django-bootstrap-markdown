from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

class Image(models.Model):
    original = models.ImageField(upload_to='markdown/images/')
    large = ImageSpecField(
        source='original',
        processors=[ResizeToFit(750, 400)],
        options={'quality': 75}
    )
    medium = ImageSpecField(
        source='original',
        processors=[ResizeToFit(375, 400)],
        options={'quality': 75}
    )
    small = ImageSpecField(
        source='original',
        processors=[ResizeToFit(185, 400)],
        options={'quality': 75}
    )
    billboard = ImageSpecField(
        source='original',
        processors=[ResizeToFill(750, 300)],
        options={'quality': 75}
    )
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']