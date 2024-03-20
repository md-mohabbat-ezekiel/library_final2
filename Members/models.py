from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
class MembersAccount(models.Model):
    user = models.OneToOneField(User,related_name ="account",on_delete=models.CASCADE)
    account_no = models.IntegerField(unique = True)
    initial_deposit_date = models.DateField(auto_now_add = True)
    balance = models.DecimalField(max_digits=12, decimal_places=2,default=Decimal('0.00'))

    def __str__(self) -> str:
        return str(self.account_no)
