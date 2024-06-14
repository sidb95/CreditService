from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import urlencode
from django.urls import reverse
from Authenticator.views import get_params
from Authenticator.models import Person
from .models import Loan, Bill, SavedState
from .LoanService import *
from rest_framework import viewsets, permissions
from .serializers import LoanSerializer, BillSerializer


class LoanViewSet(viewsets.ModelViewSet):
    
    queryset = Loan.objects.all().order_by('disbursement_date')
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]


class BillViewSet(viewsets.ModelViewSet):
    
    queryset = Bill.objects.all().order_by('bill_date')
    serializer_class = BillSerializer
    permission_classes = [permissions.IsAuthenticated]

# function ```get_params_2```
def get_params_get(request, keys):
  params = {}
  for key in keys:
    params[key] = request.GET.get(key)
  return params


# function ```apply_loan```
def apply_loan(request):
  if request.method == "GET":
    try:
      params = get_params_get(request, ['uuid', 'sid', 'messages'])
      if params['sid'] is None or params['sid'] == "":
        return redirect('Authenticator:login')
      else:
        return render(request, 'Welcome/apply_loan.html', params)
    except ValueError as err:
      print("Handling illegal request", err)
      messages.info(request, "Authentication unsuccessful")
      return redirect(request, 'Authenticator:login')
  else:
    no1 = len(SavedState.objects.all())
    ss = (SavedState.objects.all()[no1 - 1])
    uuid = ss.uuid
    sid = ss.sid
    return render(request, 'Welcome/apply_loan.html', {'uuid':uuid, 'sid':sid})


# function ```index```
def index(request):
  if request.method == "GET":
    try:
      params = get_params_get(request, ['sid', 'uuid'])
      if params['sid'] is None or params['sid'] == "":
        return redirect('Authenticator:login')
      else:
        ss = SavedState.objects.create(uuid=params['uuid'], sid=params['sid'])
        ss.save()
        return render(request, "Welcome/index.html", params)
    except ValueError as err:
      print("Handling illegal request", err)
      messages.info(request, "Authentication unsuccessful")
      return redirect(request, 'Authenticator:login')
  else:
    uid = len(Loan.objects.all()) + 1
    loan_service = LoanService(uid)
    keys = ['loan_type', 'loan_amount', 'interest_rate', 'term_period', 'disbursement_date']
    saved_states = SavedState.objects.all()
    no1 = len(saved_states)
    ss = saved_states[no1 - 1]
    uuid = ss.uuid
    sid = ss.sid
    params = get_params(request, keys)
    usr = Person.objects.get(uuid=uuid)
    if usr is not None:
      if loan_service.validate_request(params, usr.annual_income, 30):
        loan = Loan.objects.create(uid=uid, uuid=usr, loan_type=params['loan_type'],
                        loan_amount=params['loan_amount'], 
                        interest_rate=params['interest_rate'], 
                        term_period=params['term_period'], 
                        disbursement_date=params['disbursement_date'])
        loan.save()
        #
        messages.info(request, "Loan entry created successfully")
        base_url = reverse('Welcome:apply_loan')
        query_string = urlencode({'sid':sid, 'uuid':uuid, 'messages':messages})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
    else:
      messages.info(request, "Authentication unsuccessful")
      return redirect(request, 'Authenticator:login')


def make_payment(request):
  if request.method == "GET":
    params = get_params_get(request, ['sid', 'uuid'])
    return render(request, 'Welcome/make_payment.html', params)
  else:
    params = get_params(request, ['loan_id', 'amount'])
    loan_id = params['loan_id']
    amount = params['amount']
    ls1 = Payment(loan_id)
    try:
      ls1.make_payment(amount)
      messages.info(request, "Payment made successfully")
      return render(request, 'Welcome/make_payment.html', params)
    except ValueError as err:
      print("ValueError", err)
      redirect('Authenticator:login')

  def get_statement(request):
    if request.method == "GET":
      params = get_params_get(request, ['sid', 'uuid', 'loan_id'])
      loan_id = params['loan_id']
      if loan_id is not None or loan_id != "":
        ls1 = Payment(loan_id)
        context = {}
        context['sid'] = params['sid']
        context['uuid'] = params['uuid']
        context['loan_id'] = loan_id
        context['due_payments'] = ls1.getDueDates()
        context['past_transactions'] = ls1.getPastTransactions()
        base_url = reverse('Welcome:transactions')
        query_string = urlencode(context)
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
      else:
        return render(request, 'Welcome/get_statement.html', params)
