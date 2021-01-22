from django.urls import path, include

urlpatterns = [
    path('make-rsv/', ),
    path('guest-rsv/list/', ),
    path('host-rsv/list', ),
    path('<int:pk>/cancel/', ),
    path('info/', ),
]