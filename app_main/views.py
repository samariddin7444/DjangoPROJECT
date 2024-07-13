from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, "app_main/login.html")

@login_required
def home(request):
    return render(request, "app_main/home.html")
