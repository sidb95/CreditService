from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from Authenticator.models import Person

class Loan(models.Model):
  uid = models.IntegerField(unique=True)
  uuid = models.ForeignKey(Person, on_delete=models.CASCADE)
  loan_type = models.CharField(max_length=10, null=False)
  loan_amount = models.IntegerField(null=False, 
                                    validators=[MinValueValidator(150000)])
  interest_rate = models.IntegerField(null=False, 
                                      validators=[MaxValueValidator(100), 
                                                  MinValueValidator(12)])
  term_period = models.IntegerField(null=False)
  disbursement_date = models.DateField(null=False)


class Bill(models.Model):
  uid = models.IntegerField(null=False)
  loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
  amount = models.IntegerField(null=False)
  bill_date = models.DateField(null=False)
  principal_due = models.IntegerField(default=0, null=False)
  min_due = models.IntegerField(default=0, null=False)


class SavedState(models.Model):
  uuid = models.IntegerField(null=False)
  sid = models.IntegerField(default=1, null=False)
