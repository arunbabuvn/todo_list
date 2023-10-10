from django.urls import path
from base import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register, name="register"),
    path("newTask", views.new_task, name="newTask"),
]
