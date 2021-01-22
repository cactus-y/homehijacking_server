from django.urls import path, include
from . import views

urlpatterns = [
    path('info/', views.RoomDetailAPI.as_view()),
    path('list/', views.RoomListAPI.as_view()),
    path('create/', views.RoomCreateAPI.as_view()),
]