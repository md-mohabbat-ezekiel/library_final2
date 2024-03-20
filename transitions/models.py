from django.db import models
from Members.models import MembersAccount

class Transaction(models.Model):
    account = models.ForeignKey(MembersAccount,on_delete=models.CASCADE, related_name = 'transactions')
    amount = models.DecimalField(max_digits = 12 , decimal_places = 2)
    balance_after_transaction = models.DecimalField(max_digits = 12 ,decimal_places = 2)
    timestamp = models.DateTimeField(auto_now_add = True)
    

    class Meta :
        ordering = ['timestamp']
    
    def __str__(self) -> str:
        return str(self.account)