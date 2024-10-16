import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')
    in_stock = django_filters.BooleanFilter(field_name='stock', widget=django_filters.widgets.BooleanWidget())

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'in_stock']