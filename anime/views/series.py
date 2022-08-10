from rest_framework import generics

from anime.models.series import SeriesModel
from anime.serializers.series import SeriesListSerializer, SeriesDetailSerializer


class SeriesListView(generics.ListAPIView):
    queryset = SeriesModel.objects.all()
    serializer_class = SeriesListSerializer


class SeriesDetailView(generics.RetrieveAPIView):
    queryset = SeriesModel.objects.all()
    serializer_class = SeriesDetailSerializer
