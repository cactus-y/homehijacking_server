from rest_framework import serializers
from .models import Room
from users.serializers import UserSerializer
from rest_framework.exceptions import ValidationError

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'host',
            'room_image',
            'max_guest',
            'memo'
        )

