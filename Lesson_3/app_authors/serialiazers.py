from rest_framework.serializers import ModelSerializer
from .models import AuthorModel, BiographyModel, BookModel

class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'

class BiographyModelSerializer(ModelSerializer):
    class Meta:
        model = BiographyModel
        fields = '__all__'

class BookModelSerializer(ModelSerializer):

    #author = AuthorModelSerializer(many=True)

    class Meta:
        model = BookModel
        fields = '__all__'