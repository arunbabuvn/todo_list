from django.urls import path, include
from base import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", views.login_page, name="login"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("newTask/", views.new_task, name="newTask"),
    path("editTask/<str:pk>", views.edit_task, name="editTask"),
    path("delete/<str:pk>/", views.delete, name="delete"),
]
