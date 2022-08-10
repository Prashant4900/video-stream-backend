from rest_framework import serializers

from anime.models.categories import CategoriesModel


class CategoriesListSerializer(serializers.ModelSerializer):
    '''
    Categories List Serializer return list of categories.\n
    ```[
        {
            "id": 1,
            "name": "Action"
        },
        .....
        {
            "id": 4,
            "name": "Drama"
        }
    ]
    ```
    '''
    class Meta:
        model = CategoriesModel
        fields = ('id', 'name')


class CategoriesDetailSerializer(serializers.ModelSerializer):
    """
    Category Detail Serializer return detail of category 
    along with list of series in that category.
    ```
    {
        "id": 1,
        "name": "Action",
        "series_categories": [
            2,
            3
        ]
    }
    ```
    """
    class Meta:
        model = CategoriesModel
        fields = ('id', 'name', 'series_categories')
