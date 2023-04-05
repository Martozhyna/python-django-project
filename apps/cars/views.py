from django.http import Http404
from rest_framework import status
from rest_framework.generics import get_object_or_404, GenericAPIView,ListAPIView,ListCreateAPIView, RetrieveAPIView, \
    CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer, CarListSerializer


# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()


    def get_serializer_class(self):
        return CarSerializer if self.request.method !='GET' else CarListSerializer

    def get_queryset(self):
        qs = CarModel.objects.all()
        params_dict = self.request.query_params.dict()

        if 'year' in params_dict:
            qs = qs.filter(year__gte=params_dict['year'])

        return qs


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer














