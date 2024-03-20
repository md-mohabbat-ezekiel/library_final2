from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView,View
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.contrib.auth import login,logout
from django.contrib.auth.models import User

class RegistrationFormView(CreateView):
    template_name = 'register.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
       
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request, 'SignUp in information incorrect')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context
    
class UserLoginView(LoginView):
    template_name ='register.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.warning(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


# @method_decorator(login_required, name= 'dispatch')
# class logOut(LogoutView):
   
#     def get_success_url(self):
#        messages.success(self.request, "You have been successfully logged out.")
#        return reverse_lazy('login')


def logOut(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')
