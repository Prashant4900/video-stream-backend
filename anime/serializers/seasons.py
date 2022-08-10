from rest_framework import serializers

from anime.models.seasons import SeasonsModel
from anime.models.series import SeriesModel
from anime.serializers.media import ImageSerializer
from anime.serializers.episodes import NestedEpisodeSerializer


class SeasonEpisodeDetailListSerializer(serializers.ModelSerializer):
    class NestedSeriesSerializer(serializers.ModelSerializer):
        class Meta:
            model = SeriesModel
            fields = ('id',)

    thumbnail = ImageSerializer()
    episodes_season = NestedEpisodeSerializer(many=True)
    series = NestedSeriesSerializer()

    class Meta:
        model = SeasonsModel
        fields = ('id', 'name', 'no', 'series', 'description',
                  'thumbnail', 'episodes_season')
        depth = 1


class NestedSeasonSerializer(serializers.ModelSerializer):
    thumbnail = ImageSerializer()

    class Meta:
        model = SeasonsModel
        fields = ('id', 'name', 'no', 'description', 'thumbnail')
        depth = 1
