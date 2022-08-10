from rest_framework import serializers

from anime.models.series import SeriesModel
from anime.serializers.media import ImageSerializer
from anime.serializers.seasons import NestedSeasonSerializer


class SeriesListSerializer(serializers.ModelSerializer):
    poster = ImageSerializer()
    banner = ImageSerializer()

    class Meta:
        model = SeriesModel
        exclude = ('create_at', 'update_at')
        depth = 0


class SeriesDetailSerializer(serializers.ModelSerializer):
    poster = ImageSerializer()
    banner = ImageSerializer()
    seasons_series = NestedSeasonSerializer(many=True)

    class Meta:
        model = SeriesModel
        fields = ('id', 'title', 'slug', 'synopsis', 'poster',
                  'banner', 'adult', 'tags', 'categories', 'seasons_series')
        depth = 1
