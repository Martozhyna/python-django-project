from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.permissions.is_superuser import IsSuperuser
from core.services.email_service import EmailService

from apps.users.models import UserModel as User

from .serializers import UserSerializer

UserModel: User = get_user_model()


class UserToAdminView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestSendEmailView(GenericAPIView):
    def get(self, *args, **kwargs):
        EmailService.send_email({'user': 'Max'})
        return Response(status=status.HTTP_200_OK)
