from .models import Loan, Bill
from rest_framework import serializers


class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan
        fields = ['uid', 'uuid', 'loan_type', 'loan_amount', 'interest_rate', 
                  'term_period', 'disbursement_date']


class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ['uid', 'loan_id', 'amount', 'bill_date' 'principal_due', 
                  'min_due', 'term']
