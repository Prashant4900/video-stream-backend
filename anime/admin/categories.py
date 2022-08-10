from typing import Sequence

from django.contrib import admin

from anime.models.categories import CategoriesModel


class CategoriesAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = ('id', 'name', 'update_at', 'create_at')
    list_display_links: Sequence[str] = ('id', 'name')
    list_filter: Sequence[str] = ('update_at', 'create_at')
    search_fields: Sequence[str] = ('name',)
    ordering: Sequence[str] = ('name',)
    list_per_page: int = 25

    class Meta:
        model = CategoriesModel
        fields = '__all__'
