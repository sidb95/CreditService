from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import urlencode
from django.urls import reverse
from Authenticator.views import get_params
from Authenticator.models import Person
from .models import Loan, SavedState
from .LoanService import *


# function ```get_params_2```
def get_params_get(request, keys):
  params = {}
  for key in keys:
    params[key] = request.GET.get(key)
  return params


# function ```apply_loan```
def apply_loan(request):
  if request.method == "POST":
    loan_service = LoanService()
    uid = len(Loan.objects.all()) + 1
    keys = ['loan_type', 'loan_amount', 'interest_rate', 'term_period', 'disbursement_date']
    no1 = len(SavedState.objects.all())
    ss = (SavedState.objects.all()[no1 - 1])
    uuid = ss.uuid
    params = get_params(request, keys)
    usr = Person.objects.get(uuid=uuid)
    if usr is not None:
      if loan_service.validate_request(params):
        loan = Loan.objects.create(uid=uid, uuid=usr, loan_type=params['loan_type'],
                        loan_amount=params['loan_amount'], 
                        interest_rate=params['interest_rate'], 
                        term_period=params['term_period'], 
                        disbursement_date=params['disbursement_date'])
        loan.save()
        #
        messages.info(request, "Loan entry created successfully")
        return redirect(request, "Welcome:apply_loan")
      else:
        return redirect('Welcome:index')
    else:
      messages.info(request, "Authentication unsuccessful")
      return redirect(request, 'Authenticator:login')


# function ```index```
def index(request):
  if request.method == "GET":
    try:
      params = get_params_get(request, ['sid', 'uuid'])
      if params['sid'] is None or params['sid'] == "":
        redirect('Authenticator:login')
      else:
        ss = SavedState.objects.create(uuid=params['uuid'])
        ss.save()
        return render(request, "Welcome/index.html", params)
    except ValueError as err:
      print("Handling illegal request", err)
      messages.info(request, "Authentication unsuccessful")
      return redirect(request, 'Authenticator:login')
  else:
    return apply_loan(request)
