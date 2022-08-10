from django.urls import path

from .views import categories
from .views import tags
from .views import series
from .views import seasons

urlpatterns = [
    # Categories URLs
    path('category/<int:pk>/',
         categories.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/', categories.CategoriesView.as_view(), name='categories'),

    # Tags URLs
    path('tag/<int:pk>/', tags.TagDetailView.as_view(), name='tag-detail'),
    path('tags/', tags.TagsListView.as_view(), name='tags'),

    # Series URLs
    path('series/<int:pk>/', series.SeriesDetailView.as_view(), name='series-detail'),
    path('series/', series.SeriesListView.as_view(), name='series'),

    # Seasons URLs
    path('season/<int:pk>/', seasons.SeasonEpisodeDetailListAPIView.as_view(),
         name='season-detail'),
]
