from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = 'id', 'model', 'year', 'price', 'auto_park'


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = 'id', "model", 'price',
