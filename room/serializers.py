from rest_framework import serializers
from .models import Room
from users.serializers import UserSerializer

class RoomSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    class Meta:
        model = Room
        fields = (
            'host',
            'room_image',
            'max_guest',
            'memo'
        )