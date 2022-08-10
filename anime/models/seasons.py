from django.db import models
from django.utils.html import mark_safe

from filer.fields.image import FilerImageField

# Create your models here.


class SeasonsModel(models.Model):
    name = models.CharField(max_length=20)
    no = models.IntegerField(default=0)
    series = models.ForeignKey(
        'SeriesModel', on_delete=models.CASCADE, related_name='seasons_series')
    description = models.TextField(null=True, blank=True)
    thumbnail = FilerImageField(
        null=True, blank=True, on_delete=models.CASCADE, related_name='season_thumbnail')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def image_preview_method(self, url: str):
        return mark_safe(f'<div class="image"><img src="{url}" alt="image-preview"/></div>')

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return self.image_preview_method(self.thumbnail.url)
        return ""

    class Meta:
        db_table = 'seasons'
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'
