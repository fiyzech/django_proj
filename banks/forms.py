from django import forms
from .models import Bank

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['id', 'bank_name', 'routing_number', 'swift_bic']
