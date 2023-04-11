from rest_framework.serializers import ModelSerializer, RelatedField, StringRelatedField, ValidationError

from core.dataclasses.auto_park_dataclass import AutoPark

from .models import CarModel


class AutoParkRelatedFieldSerializer(RelatedField):

    def to_representation(self, value: AutoPark):
        return {'id': value.id, 'name': value.name}


class CarSerializer(ModelSerializer):
    # auto_park = StringRelatedField()
    auto_park = AutoParkRelatedFieldSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year', 'price', 'photo', 'auto_park')
        # depth = 2 вкладеність



