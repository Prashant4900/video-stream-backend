from rest_framework import generics

from anime.models.tags import TagsModel
from anime.serializers.tags import TagsListSerializer, TagDetailSerializer


class TagsListView(generics.ListAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = TagsListSerializer


class TagDetailView(generics.RetrieveAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = TagDetailSerializer
