from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from user.models import Account

class RegisterForm(ModelForm):

    # UserCreationForm has username, password, password confirmation

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'street_number', 'street_name',
                    'suburb', 'state', 'car_license']
