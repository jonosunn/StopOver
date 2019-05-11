from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import Account

class UserForm(UserCreationForm):

    # UserCreationForm has username, password, password confirmation

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['car_license', 'mobile', 'street_number', 'street_name', 'suburb', 'postcode']
