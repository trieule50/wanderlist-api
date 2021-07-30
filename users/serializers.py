from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        field = ('id', 'email', 'username', 'password', 'avatar')
        