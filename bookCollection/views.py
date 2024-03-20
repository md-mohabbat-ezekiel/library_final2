from django.shortcuts import render
from .models import AddBook,Category,BuyBook
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.views import View
from django.contrib import messages
from . import forms
from django.utils import timezone
from django.utils.encoding import force_str
from django.contrib.auth.models import User
# Create your views here.
class BookView(View):
    template_name = 'book.html'

    def get(self, request, category_slug=None):
        data = AddBook.objects.all()
        categories = Category.objects.all()

        if category_slug is not None:
            category = Category.objects.get(slug=category_slug)
            data = AddBook.objects.filter(category=category)

        return render(request, self.template_name, {"data": data, "categories": categories})
    
    

from django.contrib.auth.models import AnonymousUser
from django.utils.encoding import force_str

class DetailsPost(DetailView):
    model = AddBook
    pk_url_kwarg = 'id'
    template_name = 'details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()

        if request.method == 'POST' and comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = post
            new_comment.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()

        user = self.request.user
        user_str = force_str(user)

        if not isinstance(user, AnonymousUser):  
            # Check if the user is not anonymous
            user_instance = User.objects.get(username=user_str) 
             # Retrieve the User instance
            has_bought_book = BuyBook.objects.filter(user=user_instance, book=post).exists()
        else:
            has_bought_book = False

        if has_bought_book:
            comment_form = forms.CommentForm()
            context['comment_form'] = comment_form

        context['comments'] = comments
        
        return context





class BookBorrowView(LoginRequiredMixin,View):
    def get(self,request,id, **kwargs):
        book = get_object_or_404(AddBook, id = id)
        user = self.request.user
        if user.account.balance > book.price:
            user.account.balance -= book.price
            messages.success(request, 'book borrowed successful Please Review This Book so Another be inspired to Read this Book ')
            user.account.save(update_fields=['balance'])
            BuyBook.objects.create(
                book = book,
                user = user,
                date=timezone.now(),
            )
    
            return redirect('profile') 
        else:
            messages.warning(request, 'Insufficient balance to borrow the book Deposit Please')
            return redirect('book')
