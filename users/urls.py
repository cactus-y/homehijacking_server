from django.urls import path, include
from . import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout'),
    path("auth/register/", views.RegistrationAPI.as_view()),
    path("auth/login/", views.LoginAPI.as_view()),
    path("auth/<int:pk>/", views.UserAPI.as_view()),
    path("auth/<int:pk>/update/", views.UserUpdateAPI.as_view()),
    path('auth/<int:pk>/friend/', views.FriendListAPI.as_view()),
    path('auth/<int:pk>/addfriend/', views.AddFriendAPI.as_view()),
]