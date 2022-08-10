from typing import Sequence, Optional

from django.contrib import admin

from anime.models.episodes import EpisodesModel


class EpisodesAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = (
        'title', 'no', 'thumbnail_preview', 'season', 'update_at')
    list_display_links: Sequence[str] = ('title', 'no')
    list_filter: Sequence[str] = ('season', 'no', 'update_at', 'create_at')
    search_fields: Sequence[str] = (
        'title', 'subtitle', 'season__name', 'season__series__title', 'season__series__type')
    ordering: Sequence[str] = ('title',)
    list_per_page: int = 25
    save_on_top: bool = True

    class Meta:
        model = EpisodesModel
        fields = '__all__'

    class Media:
        model = EpisodesModel
        fields = '__all__'
        css = {
            'all': ('anime/css/style.css',)
        }


class EpisodeInline(admin.StackedInline):
    model = EpisodesModel
    extra: int = 0
    min_num: Optional[int] = 0
