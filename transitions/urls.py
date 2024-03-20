
from django.urls import path,include
from .views import DepositMoneyView


urlpatterns = [
  path('deposit/',DepositMoneyView.as_view(),name='deposit')
]