from typing import Sequence, Optional, Dict

from django.contrib import admin
from django.utils.translation import gettext as _

from anime.models.movies import MoviesModel


class MoviesAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = (
        'title', 'adult', 'banner_preview', 'poster_preview', 'series', 'update_at')
    list_display_links: Sequence[str] = ('title', 'adult')

    fieldsets = (
        ('Title', {'fields': ('title', 'slug')}),
        (_('Movies Information'), {
         'fields': ('synopsis', 'adult', 'source')}),
        (_('Images'), {
            'fields': ('series', 'poster', 'banner')}),
        (_('Meta'), {'fields': ('update_at', 'create_at')}),
    )

    filter_horizontal: Sequence[str] = ('categories', 'tags')
    list_filter: Sequence[str] = (
        'adult', 'categories', 'tags', 'update_at',  'create_at')
    search_fields: Sequence[str] = (
        'title', 'synopsis', 'categories__name', 'tags__name', 'adult', 'series__title', 'series__type', )
    ordering: Optional[Sequence[str]] = ('title',)

    readonly_fields: Sequence[str] = (
        'update_at', 'create_at', 'banner_preview', 'poster_preview')
    save_on_top: bool = True
    list_per_page: int = 25

    class Media:
        model = MoviesModel
        fields = '__all__'
        css = {
            'all': ('anime/css/style.css',)
        }
