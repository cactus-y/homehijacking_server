from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User

# Create your views here.

# @require_POST
# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 username=request.POST['username'],
#                 email=request.POST['email'],
#                 nickname=request.POST['nickname'],
#                 realname=request.POST['realname'],
#                 phone_num=request.POST['phone_num'],
#                 host_or_guest=request.POST['host_or_guest'],
#                 address=request.POST['address'],
#                 password=request.POST['password1']
#             )
#             auth.login(request, user)
#             return redirect('/room/search/')
#         return render(request, 'signup.html')
#     else:
#         return render(request, 'signup.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/room/search/')
#         else:
#             return render(request, 'login.html', {'error': 'username or password is invalid'})
#     else:
#         return render(request, 'login.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/users/login/')
