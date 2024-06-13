from django.shortcuts import render, redirect
from django.contrib import messages
from Authenticator.views import get_params
from Authenticator.models import Person
from .models import Loan

def get_params_2(request, keys):
  params = {}
  for key in keys:
    params[key] = request.GET.get(key)
  return params

def index(request):
  if request.method == "GET":
    try:
      params = get_params_2(request, ['sid', 'uuid'])
      if params['sid'] is None or params['sid'] == "":
        redirect('Authenticator:login')
      else:
        return render(request, "Welcome/index.html", params)
    except ValueError as err:
      print("Handling illegal request", err)
      messages.info(request, "Authentication not successful")
      return render(request, 'Authenticator/login.html')
  else:
    uid = len(Loan.objects.all()) + 1
    keys = ['uuid', 'loan_type', 'loan_amount', 'interest_rate', 'term_period', 
            'disbursement_date']
    params = get_params(request, keys)
    usr = Person.objects.get(uuid=params['uuid'])
    loan = Loan.objects.create(uid=uid, uuid=usr, loan_type=params['loan_type'],
                               loan_amount=params['loan_amount'], 
                               interest_rate=params['interest_rate'], 
                               term_period=params['term_period'], 
                               disbursement_date=params['disbursement_date'])
    loan.save()
    messages.info(request, "Loan entry created successfully")
    context = params
    return render(request, "Welcome/index.html", context)
