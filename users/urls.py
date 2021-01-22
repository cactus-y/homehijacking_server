from django.urls import path, include
from . import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout'),
    path("auth/register/", views.RegistrationAPI.as_view()),
    path("auth/login/", views.LoginAPI.as_view()),
    path("auth/user/", views.UserAPI.as_view()),
    path("auth/user/<int:pk>/update/", views.UserUpdateAPI.as_view()),
    path('auth/user/friend/', views.FriendListAPI.as_view()),
    path('auth/user/addfriend/', views.AddFriendAPI.as_view()),
]