from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsAuthenticated,)

