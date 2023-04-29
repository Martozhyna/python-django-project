from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from drf_yasg.utils import swagger_auto_schema

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, PasswordRecoveryToken, SocketToken

from apps.auth.serializers import AuthPasswordSerializer, EmailSerializer, TokenPairSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

from .swagger.decorators import activate_user_swagger, auth_register_swagger, token_pair_swagger

UserModel: User = get_user_model()


@token_pair_swagger()
class TokenPairView(TokenObtainPairView):
    """
       Login
    """
    serializer_class = TokenPairSerializer


@auth_register_swagger()
class AuthRegisterView(CreateAPIView):
    """
       Register user
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


@activate_user_swagger()
class ActivateUserView(GenericAPIView):
    """
    Activate User by token
    """
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class PasswordRecoveryView(GenericAPIView):
    """
        Request for password recovery
    """
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: 'Password change request sent'}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=data['email'])
        EmailService.password_recovery(user)
        return Response('Password change request sent', status=status.HTTP_200_OK)


class PasswordChangeView(GenericAPIView):
    """
        Set recovery password
    """
    permission_classes = (AllowAny,)
    serializer_class = AuthPasswordSerializer

    @atomic
    @swagger_auto_schema(responses={status.HTTP_200_OK: ''}, security=[])
    def post(self, *args, **kwargs):
        token = kwargs['token']
        user: User = JWTService.validate_token(token, PasswordRecoveryToken)
        data = self.request.data
        serializer = AuthPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user.set_password(data['password'])
        user.save()
        return Response(status=status.HTTP_200_OK)


class SocketTokenView(GenericAPIView):
    def get(self, *args, **kwargs):
        user = self.request.user
        token = JWTService.create_token(user, SocketToken)
        return Response({'token': str(token)}, status.HTTP_200_OK)

