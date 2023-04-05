from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer, CarListSerializer


class CarListCreateView(APIView):

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarListSerializer(instance=cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data: dict = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



