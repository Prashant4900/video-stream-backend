from rest_framework import serializers

from anime.models.episodes import EpisodesModel
from anime.serializers.media import ImageSerializer


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodesModel
        fields = '__all__'
        exclude = ('create_at', 'update_at')


class NestedEpisodeSerializer(serializers.ModelSerializer):
    thumbnail = ImageSerializer()

    class Meta:
        model = EpisodesModel
        fields = ('title', 'subtitle', 'no', 'source', 'thumbnail')
        depth = 1
