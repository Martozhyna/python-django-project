from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        qs = CarModel.objects.all()
        params_dict = self.request.query_params.dict()

        if 'year' in params_dict:
            qs = qs.filter(year__gte=params_dict['year'])

        return qs


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
