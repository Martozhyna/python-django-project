
from django_filters import rest_framework as filters

from apps.cars.models import CarModel


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    brand_start = filters.CharFilter(field_name='model', lookup_expr='istartswith')
    brand_end = filters.CharFilter(field_name='model', lookup_expr='endswith')
    brand_contain = filters.CharFilter(field_name='model', lookup_expr='icontains')

    class Meta:
        model = CarModel
        fields = ('year_gt', 'year_lt', 'brand_start', 'price_gt', 'price_lt', 'price_gte')
