from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, PasswordRecoveryToken

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class PasswordRecoveryView(GenericAPIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        user = get_object_or_404(UserModel, email=data['email'])
        EmailService.password_recovery(user)
        return Response('Password change request sent', status=status.HTTP_200_OK)


class PasswordChangeView(GenericAPIView):

    def post(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, PasswordRecoveryToken)
        data = self.request.data
        serializer = UserSerializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        user.set_password(data['password'])
        user.save()
        return Response('Password successfully changed', status=status.HTTP_200_OK)




