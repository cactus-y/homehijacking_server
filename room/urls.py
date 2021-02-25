from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.RoomDetailAPI.as_view()),
    path('list/', views.RoomListAPI.as_view()),
    path('<int:pk>/', views.RoomCreateAPI.as_view()),
]