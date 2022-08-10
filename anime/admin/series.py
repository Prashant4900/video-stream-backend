from typing import Sequence, Optional, Dict

from django.contrib import admin
from django.utils.translation import gettext as _

from anime.models.series import SeriesModel


class SeriesAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = (
        'title', 'adult', 'banner_preview', 'poster_preview', 'type', 'update_at')
    list_display_links: Sequence[str] = ('title', 'adult')
    prepopulated_fields: Dict[str, Sequence[str]] = {'slug': ('title',)}

    fieldsets = (
        ('Title', {'fields': ('title', 'slug')}),
        (_('Series Information'), {
         'fields': ('type', 'synopsis', 'adult')}),
        (_('Images'), {
            'fields': ('poster', 'banner')}),
        (_('Groups'), {'fields': ('categories', 'tags')}),
        (_('Meta'), {'fields': ('update_at', 'create_at')}),
    )

    filter_horizontal: Sequence[str] = ('categories', 'tags')
    list_filter: Sequence[str] = (
        'adult', 'type', 'categories', 'tags', 'update_at',  'create_at')
    search_fields: Sequence[str] = (
        'title', 'synopsis', 'categories__name', 'tags__name', 'adult', 'type')
    ordering: Optional[Sequence[str]] = ('title',)

    readonly_fields: Sequence[str] = (
        'update_at', 'create_at', 'banner_preview', 'poster_preview')
    save_on_top: bool = True
    list_per_page: int = 25

    class Media:
        model = SeriesModel
        fields = '__all__'
        css = {
            'all': ('anime/css/style.css',)
        }
