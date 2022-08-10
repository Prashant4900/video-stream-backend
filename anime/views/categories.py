from rest_framework import generics

from anime.models.categories import CategoriesModel
from anime.serializers.categories import CategoriesListSerializer, CategoriesDetailSerializer


# Create your views here.
class CategoriesView(generics.ListAPIView):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesListSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesDetailSerializer
