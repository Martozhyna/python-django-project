from rest_framework.serializers import ModelSerializer, RelatedField, StringRelatedField

from core.dataclasses.auto_park_dataclass import AutoPark

from apps.cars.models import CarModel


class AutoParkRelatedFieldSerializer(RelatedField):

    def to_representation(self, value: AutoPark):
        return {'id': value.id, 'name': value.name}


class CarSerializer(ModelSerializer):
    # auto_park = StringRelatedField()
    auto_park = AutoParkRelatedFieldSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year', 'price', 'auto_park')
        # depth = 2 вкладеність


class CarListSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', "model", 'price', 'auto_park')
