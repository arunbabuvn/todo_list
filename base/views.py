from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "todo.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, "registration/login.html", context)

        login(request, user)
        return redirect("/")

    return render(request, "registration/login.html")


def register(request):
    return render(request, "registration/register.html")


def new_task(request):
    return render(request, "newTask.html")
