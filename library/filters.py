import django_filters
from .models import Author


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains"
    )  # фильтрация по имени, чувствительность к регистру отключена

    class Meta:
        model = Author
        fields = ["name"]
