from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAdminUser, BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import AuthorModel, BiographyModel, BookModel
from .serialiazers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer
from .filters import BookFilter


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class AuthorModelViewSet(ModelViewSet):
    #renderer_classes = [JSONRenderer]
    #permission_classes = [IsAdminUser] #Только для Админов
    #permission_classes = [StaffOnly]
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorModelSerializer

class BiographyModelViewSet(ModelViewSet):
    queryset = BiographyModel.objects.all()
    serializer_class = BiographyModelSerializer

class BookModelViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer

    #def get_queryset(self):
    #    name = self.request.query_params.get('name', '')
    #    book = BookModel.objects.all()

    #    if name:
    #        book = book.filter(name__contains=name)
    #    return book

class BookDjangoFilterViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer
    #filterset_fields = ['id', 'name']
    filterset_class = BookFilter

# PAGINATOR

class BookLimitOffsetPaginaton(LimitOffsetPagination):
    default_limit = 3

class BookLimitOffsetPaginatonViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = BookLimitOffsetPaginaton
