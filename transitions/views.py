from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Transaction
from .forms import DepositForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_Mail(user,amount,mail_subject,template):
        message= render_to_string(template, {
                "user": user,
                "amount": amount,
            })
        send_email =EmailMultiAlternatives(mail_subject,"", to=[user.email])
        send_email.attach_alternative(message,'text/html')
        send_email.send()


class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs  = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        
        })
        return kwargs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # template e context data pass kora
        context.update({
            'title':self.title
        })
        return context
    

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        account.balance += amount 
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_Mail(self.request.user,amount,'Deposit Message','deposit_email.html')
        return super().form_valid(form)
