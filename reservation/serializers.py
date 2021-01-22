from rest_framework import serializers
from .models import Reservation
from users.serializers import UserSerializer
from room.serializers import RoomSerializer

class ReservationSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    guest = UserSerializer(read_only=True)
    class Meta:
        model = Reservation
        fields = (
            'room',
            'guest',
            'rsv_start_date',
            'rsv_end_date'
        )