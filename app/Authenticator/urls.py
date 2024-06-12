from django.urls import path
from django.conf.urls import include
from . import views

app_name = "Authenticator"

urlpatterns = [
    path("/api/register-user", views.index, name="index"),
    path("Authenticator/login.html", views.login, name="login")
]
