from django_filters import rest_framework as filters
from .models import BookModel

class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = BookModel
        fields = ['id', 'name']