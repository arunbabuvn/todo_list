from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from base.models import TaskData


# Create your views here.
def home(request):
    data = TaskData.objects.all()
    return render(request, "todo.html", {"data": data})


def delete(request, pk):
    data = TaskData.objects.get(id=pk)
    data.delete()
    return redirect("/")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            context = {"error": "Invalid username or password."}
            return render(request, "registration/login.html", context)
        return redirect("home")
    return render(request, "registration/login.html")


def register(request):
    return render(request, "registration/register.html")


def logout(request):
    logout(request)


def profile(request):
    return render(request, "profile.html")


def new_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        data = TaskData(title=title, description=description)
        data.save()
        return redirect("/")
    return render(request, "newTask.html")


def edit_task(request, pk):
    data = TaskData.objects.get(id=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        data = TaskData(id=pk, title=title, description=description)
        data.save()
        return redirect("/")
    return render(request, "editTask.html", {"data": data})
