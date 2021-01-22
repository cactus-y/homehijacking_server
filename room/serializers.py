from rest_framework import serializers
from .models import Room
from users.serializers import UserSerializer
from rest_framework.exceptions import ValidationError

class RoomSerializer(serializers.ModelSerializer):
    # host = UserSerializer(read_only=True)
    class Meta:
        model = Room
        fields = (
            'host',
            'room_image',
            'max_guest',
            'memo'
        )

class RoomCreateSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    class Meta:
        model = Room
        fields = (
            'host',
            'room_image',
            'max_guest',
            'memo'
        )
    
    def create(self, validated_data):
        room = Room.objects.create(
            validated_data['user'],
            validated_data['room_image'],
            validated_data['max_guest'],
            validated_data['memo']
        )
        return room