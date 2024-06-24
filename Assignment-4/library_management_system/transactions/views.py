from django.shortcuts import render
from transactions.forms import DepositForm
from transactions.models import Transaction
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class DepositMoneyView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = DepositForm
    template_name = 'deposit_form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        account.balance += amount
        account.save(
            update_fields=['balance']
        )
        return super().form_valid(form)