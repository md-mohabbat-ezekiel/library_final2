from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect,render
from django.views.generic import ListView,View
from bookCollection.models import BuyBook
from django.contrib import messages

class BookListView(LoginRequiredMixin, ListView):
    model = BuyBook
    template_name = 'profile.html'
    context_object_name = 'borrowers'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = BuyBook.objects.filter(user_id=user_id)
        return queryset

class ReturnBookView(LoginRequiredMixin, View):
    def get(self,request,id, **kwargs):
        book = get_object_or_404(BuyBook, id = id)
        user = self.request.user
        user.account.balance += book.book.price
        messages.success(request, 'book return successful')
        user.account.save(update_fields=['balance'])
        # send_email(user,book.book.price, 'return_book', 'Book Return Message','transactions/email_template.html')
        book.delete()
        return redirect('profile') 
