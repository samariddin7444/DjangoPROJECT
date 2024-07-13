from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "app_users/home.html")



def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")

        return redirect("login")

    return render(request, "app_users/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


def register_user(request):
    if request.POST:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username and password1 and password2 and password1 == password2:
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.set_password(password2)
            user.save()
            return redirect("login")

    return render(request, "app_users/register.html")
