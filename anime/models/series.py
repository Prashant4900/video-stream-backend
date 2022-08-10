from django.db import models
from django.utils.html import mark_safe

from .categories import CategoriesModel
from .tags import TagsModel

from filer.fields.image import FilerImageField

SERIES_CHOICES = (
    ("1", "TV Show"),
    ("2", "Movies"),
    ("3", "Both"),
)


class SeriesModel(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    synopsis = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=1, choices=SERIES_CHOICES)
    categories = models.ManyToManyField(
        CategoriesModel, blank=True, related_name='series_categories')
    tags = models.ManyToManyField(
        TagsModel, blank=True, related_name='series_tags')
    adult = models.BooleanField(default=False)
    poster = FilerImageField(
        null=True, blank=True, on_delete=models.CASCADE, related_name='series_poster')
    banner = FilerImageField(
        null=True, blank=True, on_delete=models.CASCADE, related_name='series_banner')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def image_preview_method(self, url: str):
        return mark_safe(f'<div class="image"><img src="{url}" alt="image-preview"/></div>')

    @property
    def banner_preview(self):
        if self.banner:
            return self.image_preview_method(self.banner.url)
        return ""

    @property
    def poster_preview(self):
        if self.poster:
            return self.image_preview_method(self.poster.url)
        return ""

    def save(self, *args, **kwargs):
        title = self.title.lower()
        self.slug = title.replace(' ', '-')
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'series'
        verbose_name = 'Series'
        verbose_name_plural = 'Series'
