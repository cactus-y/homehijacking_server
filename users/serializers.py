from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, FriendModel


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nickname',
            'realname',
            'phone_num',
            'host_or_guest',
            'address',
            "password"
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['nickname'],
            validated_data['realname'],
            validated_data['phone_num'],
            validated_data['host_or_guest'],
            validated_data['address'],
            validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nickname',
            'realname',
            'phone_num',
            'host_or_guest',
            'address',
            'password'
        )


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        return serializers.ValidationError("Unable to log in with provided credentials.")


class FriendSerializer(serializers.ModelSerializer):
    friend = UserSerializer(read_only=True, many=True)
    class Meta:
        model = FriendModel
        fields = (
            'user',
            'friend'
        )
