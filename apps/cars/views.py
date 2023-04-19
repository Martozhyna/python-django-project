from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import CarFilter
from .models import CarModel, CarPhotoModel
from .serializers import CarPhotoSerializer, CarSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny, )

    # def get_queryset(self):
    #     # qs = CarModel.objects.get_cars_by_auto_park_id(3)
    #     qs = CarModel.objects.all()
    #     params_dict = self.request.query_params.dict()
    #
    #     if 'year' in params_dict:
    #         qs = qs.filter(year__gte=params_dict['year'])
    #
    #     return qs


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarAddPhotosView(GenericAPIView):
    queryset = CarModel.objects.all()

    def post(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for key in files:
            serializer = CarPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)


class CarPhotoDeleteView(DestroyAPIView):
    queryset = CarPhotoModel.objects.all()

    def perform_destroy(self, instance):
        instance.photo.delete()
        instance.delete()
