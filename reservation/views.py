from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import ReservationSerializer
from .models import Reservation
from room.models import Room
# Create your views here.
class CreateRsvAPI(generics.GenericAPIView):
    serializer_class = ReservationSerializer

    def post(self, request):
        # room = request.room
        user = request.user

        data = request.data.copy()
        data['guest'] = user.id

        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailRsvAPI(APIView):
    def get_object(self, pk):
        return get_object_or_404(Reservation, pk=pk)

    def get(self, request, pk):
        rsv = self.get_object(pk)
        serializer = ReservationSerializer(rsv)
        return Response(serializer.data)

    def delete(self, request, pk):
        rsv = self.get_object(pk)
        rsv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GuestRsvListAPI(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user = self.request.user
        rsvlist = Reservation.objects.filter(guest=user)
        return rsvlist

class HostRsvListAPI(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user = self.request.user
        room = Room.objects.get(host=user)
        rsvlist = Reservation.objects.filter(room=room)
        return rsvlist