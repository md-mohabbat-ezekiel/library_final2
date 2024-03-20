from django import forms
from django.contrib.auth.models import User
from .models import MembersAccount
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"id":"required"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"id":"required"}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def save(self, commit=True): 
        our_user =  super().save(commit=False)  
        
        if commit:
            our_user.save() 

            # Check if MembersAccount already exists for the user
            if not MembersAccount.objects.filter(user=our_user).exists():
                MembersAccount.objects.create(
                    user=our_user,
                    account_no=10000 + our_user.id
                )

        return our_user

    



class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')