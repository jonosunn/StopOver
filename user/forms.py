from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from user.models import Account

class UserForm(UserCreationForm):

    # UserCreationForm has username, password, password confirmation
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email has already been registered.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        labels = {
            'car_license_type':'License Type',
            'car_license': 'Car License Number',
            'car_license_name':'License Full Name'
        }
        fields = [ 'mobile', 'car_license_name', 'car_license', 'car_license_type', 'street_number', 'street_name', 'suburb', 'postcode']


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email'
    )
