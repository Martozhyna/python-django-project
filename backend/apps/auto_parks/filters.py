from django_filters import rest_framework as filters

from .models import AutoParkModel


class AutoParksFilter(filters.FilterSet):
    cars_gt = filters.NumberFilter(field_name='cars', lookup_expr='year__gt')

    class Meta:
        model = AutoParkModel
        fields = ('cars_gt',)
