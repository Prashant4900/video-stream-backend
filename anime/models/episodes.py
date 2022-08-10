from django.db import models
from django.utils.html import mark_safe

from filer.fields.image import FilerImageField
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.


class EpisodesModel(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    no = models.IntegerField(default=0)
    series = models.ForeignKey(
        'SeriesModel', on_delete=models.CASCADE, related_name='episodes_series')
    season = ChainedForeignKey('SeasonsModel', chained_field='series', chained_model_field='series',
                               show_all=False, auto_choose=True, sort=True, on_delete=models.CASCADE, related_name='episodes_season')
    thumbnail = FilerImageField(
        null=True, blank=True, on_delete=models.CASCADE, related_name='episode_thumbnail')
    source = models.URLField(null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def image_preview_method(self, url: str):
        return mark_safe(f'<div class="image"><img src="{url}" alt="image-preview"/></div>')

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return self.image_preview_method(self.thumbnail.url)
        return ""

    class Meta:
        db_table = 'episodes'
        verbose_name = 'Episode'
        verbose_name_plural = 'Episodes'
