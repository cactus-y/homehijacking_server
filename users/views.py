from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User, FriendModel
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, FriendSerializer
# Create your views here.

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data['username']) < 6 or len(request.data['password']) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserUpdateAPI(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FriendListAPI(generics.ListAPIView):
    serializer_class = FriendSerializer
    
    def get_queryset(self):
        user = self.request.user
        friendlist = FriendModel.objects.filter(user=user)
        return friendlist

class AddFriendAPI(generics.GenericAPIView):
    serializer_class = FriendSerializer
    
    def put(self, request):
        user = request.user
        friendID = self.request.data['friendID']
        friend = User.objects.get(username=friendID)
        data = request.data.copy()
        data['friend'] = friend
        data['user'] = user.id
        FriendSerializer.update(self, FriendModel.objects.get(user=user), data)
        return Response(status=status.HTTP_200_OK)
        # serializer = FriendSerializer()
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     # serializer = self.get_serializer(data=request.data)
