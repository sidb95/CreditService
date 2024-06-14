from django.conf.urls import include
from django.urls import path
from . import views

app_name = "Welcome"

urlpatterns = [
    path("api/apply-loan", views.apply_loan, name="apply_loan"),
    path("api/make-payment", views.make_payment, name="make_payment"),
    path("api/get-statement", views.get_statement, name="get_statement"),
    path("Welcome/transactions.html", views.transactions, name="transactions"),
    path("Welcome/index.html", views.index, name="index")
]
