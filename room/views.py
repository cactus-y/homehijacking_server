from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RoomSerializer
from .models import Room

class RoomListAPI(generics.ListAPIView):
    serializer_class = RoomSerializer
    def get_queryset(self):
        return Room.objects.all()



class RoomDetailAPI(APIView):
    def get_object(self, user):
        return get_object_or_404(Room, host=user)

    def get(self, request):
        user = request.user
        room = self.get_object(user)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def delete(self, request):
        user = request.user
        room = self.get_object(user)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class RoomCreateAPI(generics.GenericAPIView):
    serializer_class = RoomSerializer
    
    def post(self, request):
        user = request.user

        if user.host_or_guest != 1:
            body = {"message": "guest cannot register a room"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)

        # 중복방지
        # if Room.objects.filter(host=user) != None:
        #     body = {"message": "you already registered your room"}
        #     return Response(body, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['host'] = user.id

        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
