from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.permissions.is_superuser import IsSuperuser

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

from .serializers import ProfileSerializer, UserSerializer

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


class AdminToUserView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllUsersView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        qs = UserModel.objects
        pk = self.request.user.pk
        return qs.exclude(pk=pk)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer


class UserBlockView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUnblockView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminBlockView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if not user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminUnblockView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if not user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
