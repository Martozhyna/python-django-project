from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AuthPasswordSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)
