from django.urls import path, include
from . import views

urlpatterns = [
    path('make-rsv/', views.CreateRsvAPI.as_view()),
    path('guest-rsv/list/', views.GuestRsvListAPI.as_view()),
    path('host-rsv/list/', views.HostRsvListAPI.as_view()),
    path('<int:pk>/info/', views.DetailRsvAPI.as_view()),
]