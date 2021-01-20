from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'host',
            'guest',
            'rsv_start_date',
            'rsv_end_date'
        )