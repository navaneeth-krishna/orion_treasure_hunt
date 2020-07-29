from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("register", views.register , name = 'register'),
    path("login", views.login , name = 'login'),
    path("logout",views.logout, name = 'logout'),
    path("editprofile",views.editprofile, name = 'editprofile'),
]