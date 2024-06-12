from django.conf.urls import include
from django.urls import path
from . import views

app_name = "Welcome"

urlpatterns = [
    path("Welcome/index.html", views.index, name="index")
]
