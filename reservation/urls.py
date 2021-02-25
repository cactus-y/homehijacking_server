from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.CreateRsvAPI.as_view()),
    path('list/guest/', views.GuestRsvListAPI.as_view()),
    path('list/host/', views.HostRsvListAPI.as_view()),
    path('<int:pk>/', views.DetailRsvAPI.as_view()),
]