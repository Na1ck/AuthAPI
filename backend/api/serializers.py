from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer as DjoserUserSerializer

User = get_user_model()


class UserSerializer(DjoserUserSerializer):

    class Meta(DjoserUserSerializer.Meta):
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email')
