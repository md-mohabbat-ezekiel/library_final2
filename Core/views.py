from django.shortcuts import render
from django.views.generic import TemplateView
from Members.models import MembersAccount
# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

