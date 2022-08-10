from rest_framework import generics

from anime.models.seasons import SeasonsModel
from anime.serializers.seasons import SeasonEpisodeDetailListSerializer


class SeasonEpisodeDetailListAPIView(generics.RetrieveAPIView):
    queryset = SeasonsModel.objects.all()
    serializer_class = SeasonEpisodeDetailListSerializer
