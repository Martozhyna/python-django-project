from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoParkCarsListCreateView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = self.serializer_class(auto_park.cars, many=True)
        return Response(serializer.data)
