from django.conf.urls import include
from django.urls import path
from . import views

app_name = "Welcome"

urlpatterns = [
    path("Welcome/apply_loan.html", views.apply_loan, name="apply_loan"),
    path("Welcome/index.html", views.index, name="index")
]
