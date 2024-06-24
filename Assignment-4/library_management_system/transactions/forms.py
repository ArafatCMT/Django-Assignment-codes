from django import forms
from transactions.models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.account = self.account
        return super().save()

class DepositForm(TransactionForm):

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        min_deposit_amount = 100

        if amount is None:
            raise forms.ValidationError(
                f'invalid amount'
            )
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
    
        return amount