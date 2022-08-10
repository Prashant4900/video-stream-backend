from rest_framework import serializers

from anime.models.movies import MoviesModel


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesModel
        fields = '__all__'
        exclude = ('create_at', 'update_at')
