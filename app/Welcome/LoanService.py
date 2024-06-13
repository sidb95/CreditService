import math
from .models import Loan, Bill
import datetime


"""
Class ```LoanService``` has various methods
those help apply loan to the customers.
"""
# class ```LoanService```
class LoanService():
  
  def __init__(self, loan_id):
    self.loan_id = loan_id

  # function ```getLoanId```
  def getLoanId(self, loan_id):
    return self.loan_id
  
  # function ```calc_credit_score```
  def calc_credit_score(self, balance):
    upper_limit = 1000000
    lower_limit = 10000
    answer = 300
    if balance >= upper_limit:
      answer = 900
    else:
      balance -= 10000
      answer += math.floor(((balance) / 15000) * 10)
    return answer
  
  # function ```isNULL```
  def isNULL(self, params, keys):
    for key in keys:
      if params[key] is None or params[key] == "":
        return True
    return False
  
  # function ```calcEMI```
  def calcEMI(self, loan_amt, interest_rate, days):
    billing_days = days
    apr = interest_rate
    return ((3 / 100) * loan_amt) + (round((apr / 365)) * billing_days)

  # function ```validate_request```
  def validate_request(self, params, annual_income):
    keys = ['loan_type', 'loan_amount', 'interest_rate', 'term_period', 
            'disbursement_date']
    loan_amt = int(params['loan_amount'])
    interest_rate = int(params['interest_rate'])
    if (self.isNULL(params, keys)):
      return False # Any key in keys is NULL
    elif (interest_rate < 12):
      return False # Interest rate is less than 12%
    elif (self.calc_credit_score(loan_amt) < 450):
      return False # Credit score less than 450
    elif (annual_income < 150000):
      return False # Annual income less than 150000
    elif (loan_amt > 5000):
      return False # Loan amount greater than 5000/-
    else:
      emi = self.calcEMI(loan_amt, interest_rate, 30)
      if emi > ((20 / 100) * (annual_income / 12)): 
        return False # EMI greater than 20 percent of monthly income
      if emi < 50:
        return False # EMI less than 50/-
    return True


"""
class ```Payment``` inherited from
```LoanService```
"""
# class ```LoanService```
class Payment(LoanService):
  
  # child ```init``` function
  def __init__(self, loan_id):
    super(self, loan_id) # calling the parent function (super)
    self.dateA = datetime.date(1970, 1, 1)
    self.arr1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  # function ```getLoanId```
  def getLoanId(self):
    return self.loan_id

  # function ```getPastTransactions```
  def getPastTransactions(self):
    past_transactions = []
    loan = Loan.objects.get(uid=self.getLoanId)
    interest_rate = loan.interest_rate
    bills = Bill.objects.all()
    if (len(bills) == 0):
      return []
    else:
      for bill in bills: # for each bill in bills
        transactionA = [] # a transaction object
        transactionA.append(bill.bill_date)
        transactionA.append(bill.principal_due)
        transactionA.append(interest_rate)
        transactionA.append(bill.amount)
        past_transactions.append(transactionA) # append in ```past_transactions```
    return past_transactions # returns all the past transactions

  # function ```getDueDatesAuxA1```
  def getDueDatesAuxA1(self, dateB, lastDate):
    deltaA = dateB - lastDate
    return deltaA.days
  
  # function ```getDueDatesAuxC1```
  def getDueDatesAuxC1(self, dateB, days_due):
    days_left = 31 - dateB.day
    if days_left == 0:
      return datetime.date(dateB.year, 12, 31)
    elif days_left >= days_due:
      return datetime.date(dateB.year, 12, dateB.day + days_due)
    else:
      return datetime.date(dateB.year + 1, 1, days_due - days_left)
  
  # function ```getDueDatesAuxC2```
  def getDueDatesAuxC2(self, dateB, days_due):
    days_left = self.arr1[dateB.month - 1] - dateB.day
    if days_left == 0:
      return datetime.date(dateB.year, dateB.month + 1, days_due)
    elif days_left >= days_due:
      return datetime.date(dateB.year, dateB.month, dateB.day + days_due)
    else:
      return datetime.date(dateB.year, dateB.month, days_due - days_left)
  
  # function ```getDueDatesAuxB2```
  def getDueDatesAuxB2(self, dateB, days_due):
    days_left = 29 - dateB.day
    if days_left == 0:
      return datetime.date(dateB.year, 3, days_due)
    elif days_left >= days_due:
      return datetime.date(dateB.year, 2, dateB.day + days_due)
    else:
      return datetime.date(dateB.year, 3, days_due - days_left)

  # function ```getDueDatesAuxB1```
  def getDueDatesAuxB1(self, dateB, days_due):
    if dateB.month == 12:
      return self.getDueDatesAuxC1(dateB, days_due)
    elif (dateB.year % 4 == 0):
      if dateB.month == 2:
        return self.getDueDatesAuxB2(dateB, days_due)
      elif dateB.month == 1 and dateB.day == 31 and days_due == 30:
        return datetime.date(dateB.year, 3, 1)
      elif dateB.month == 1 and dateB.day == 30 and days_due == 30:
        return datetime.date(dateB.year, 2, 29)
      else:
        return self.getDueDatesAuxC2(dateB, days_due)
    else:
      return self.getDueDatesAuxC2(dateB, days_due)

  # function ```getDueDates```
  def getDueDates(self):
    dateB = self.dateA.today()
    dues = []
    loan = Loan.objects.get(uid=self.getLoanId)
    bills = Bill.objects.all()
    no1 = len(bills)
    interest_rate = loan.interest_rate
    principal_due = loan.loan_amount
    term_period = loan.term_period
    if no1 != 0:
      lastBill = bills[no1 - 1]
      principal_due = lastBill.principal_due
      days_due = self.getDueDatesAuxA1(dateB, lastBill.bill_date)
      rem_term_period = term_period - lastBill.term
      due_date = self.getDueDatesAuxB1(dateB, days_due)
      min_due = lastBill.min_due
      principal_due = lastBill.principal_due
      if days_due == 30:
        dues.append([dateB, min_due])
        rem_term_period -= 1
      elif days_due < 30:
        dues.append([due_date, min_due])
        rem_term_period -= 1
      elif days_due <= 45:
        emi = self.calcEMI(principal_due, interest_rate, days_due - 30)
        dues.append([due_date, min_due + emi])
      else:
        print("EMI not paid on time!")
      emi = self.calcEMI(principal_due, interest_rate, 30)
      while rem_term_period != 0:
        due_date = self.getDueDatesAuxB1(due_date, 30)
        dues.append([due_date, emi])
    else:
      days_due = self.getDueDatesAuxA1(dateB, loan.disbursement_date)
      due_date = self.getDueDatesAuxB1(dateB, days_due)
      emi = self.calcEMI(principal_due, interest_rate, 30)
      dues.append([due_date, emi])
    return dues # returns upcoming dues

  # function ```make_payment```
  def make_payment(self, amount):
    loan = Loan.objects.get(uid=self.getLoanId)
    no_bills = len(Bill.objects.all()) + 1
    bill = Bill.objects.create(uid=no_bills, loan_id=loan)
    bill.amount = amount
    bill.bill_date = self.dateA.today()
    bill.term = no_bills
    if bill.min_due >= amount:
      bill.min_due -= amount
    else:
      left_off_amount = amount - bill.min_due
      bill.min_due = 0
      if left_off_amount >= bill.principal_due:
        bill.principal_due = 0
      else:
        bill.principal_due -= left_off_amount
    bill.save()
