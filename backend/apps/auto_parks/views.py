from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.services.jwt_service import JWTService, SocketToken

from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer

from .filters import AutoParksFilter
from .models import AutoParkModel


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = AutoParksFilter
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoParkCreateListCarsView(CreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)

    def get(self, *args, **kwargs):
        print(self.request.user.is_active)
        auto_park = self.get_object()
        serializer = self.serializer_class(auto_park.cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


