from rest_framework.viewsets import ModelViewSet
from .models import AuthorModel, BiographyModel, BookModel
from .serialiazers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorModelSerializer

class BiographyModelViewSet(ModelViewSet):
    queryset = BiographyModel.objects.all()
    serializer_class = BiographyModelSerializer

class BookModelViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer