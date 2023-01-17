from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')

    return render(request, 'register.html')
