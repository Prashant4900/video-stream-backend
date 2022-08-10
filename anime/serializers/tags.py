from rest_framework import serializers

from anime.models.tags import TagsModel


class TagsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsModel
        fields = ('id', 'name')


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsModel
        fields = ('id', 'name', 'series_tags')
