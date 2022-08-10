from typing import Sequence

from django.contrib import admin
from django.utils.translation import gettext as _


from anime.admin.episodes import EpisodeInline
from anime.models.seasons import SeasonsModel


class SeasonsAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = (
        'name', 'no', 'thumbnail_preview', 'series', 'update_at')
    list_display_links: Sequence[str] = ('name', 'no')
    list_filter: Sequence[str] = ('series', 'no', 'update_at', 'create_at')
    search_fields: Sequence[str] = ('name',)
    ordering: Sequence[str] = ('name',)
    list_per_page: int = 25
    save_on_top: bool = True
    inlines = (EpisodeInline,)

    class Meta:
        model = SeasonsModel
        fields = '__all__'

    class Media:
        model = SeasonsModel
        fields = '__all__'
        css = {
            'all': ('anime/css/style.css',)
        }
