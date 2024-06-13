from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from Authenticator.models import Person

class Loan(models.Model):
  uid = models.IntegerField(unique=True)
  uuid = models.ForeignKey(Person, on_delete=models.CASCADE)
  loan_type = models.CharField(max_length=10, null=False)
  loan_amount = models.IntegerField(null=False)
  interest_rate = models.IntegerField(null=False, 
                                      validators=[MaxValueValidator(100), 
                                                  MinValueValidator(12)])
  term_period = models.IntegerField(null=False)
  disbursement_date = models.DateField(null=False)
