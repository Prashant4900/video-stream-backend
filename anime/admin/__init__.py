from django.contrib import admin

from .categories import CategoriesAdmin
from .episodes import EpisodesAdmin
from .seasons import SeasonsAdmin
from .series import SeriesAdmin
from .tags import TagsAdmin
from .movies import MoviesAdmin

from anime.models.categories import CategoriesModel
from anime.models.episodes import EpisodesModel
from anime.models.seasons import SeasonsModel
from anime.models.series import SeriesModel
from anime.models.tags import TagsModel
from anime.models.movies import MoviesModel

admin.site.register(CategoriesModel, CategoriesAdmin)
admin.site.register(EpisodesModel, EpisodesAdmin)
admin.site.register(SeasonsModel, SeasonsAdmin)
admin.site.register(SeriesModel, SeriesAdmin)
admin.site.register(TagsModel, TagsAdmin)
admin.site.register(MoviesModel, MoviesAdmin)
