import math
"""
Class ```LoanService``` has various methods
those help apply loan to the customers.
"""
# class ```LoanService```
class LoanService():
  
  def __init__(self):
    pass
  
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
  def calcEMI(self, loan_amt, interest_rate):
    billing_days = 30
    apr = interest_rate
    return ((3 / 100) * loan_amt) + (round((apr / 365)) * billing_days)

  # function ```validate_request```
  def validate_request(self, params):
    keys = ['loan_type', 'loan_amount', 'interest_rate', 'term_period', 
            'disbursement_date']
    loan_amt = int(params['loan_amount'])
    interest_rate = int(params['interest_rate'])
    annual_income = int(params['annual_income'])
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
      emi = self.calcEMI(loan_amt, interest_rate)
      if emi > ((20 / 100) * (annual_income / 12)): 
        return False # EMI greater than 20 percent of monthly income
      if emi < 50:
        return False # EMI less than 50/-
    return True