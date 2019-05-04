from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Account

class RegisterForm(UserCreationForm):

    # UserCreationForm has username, password, password confirmation

    # first_name = forms.CharField(label="First Name", max_length=12)
    # last_name = forms.CharField(label="Last Name", max_length=12)
    # street_number = forms.CharField(label="Street Number", max_length=4)
    # street_name = forms.CharField(label="Street Name", max_length=12)
    # suburb = forms.CharField(label="Suburb", max_length=12)
    # STATE_CHOICES = (
    #     ('VIC', 'Victoria'),
    #     ('NSW', 'New South Wales'),
	# 	('QLD', 'Queensland'),
	# 	('TAS', 'Tasmania'),
	# 	('SA', 'South Australia'),
	# 	('ACT', 'Australia Captial Territory'),
	# 	('NT', 'Northern Territory'),
	# 	('WA', 'Western Australia')
    # )
    # state = forms.CharField(max_length=3, choices=STATE_CHOICES)

    class Meta:
        model = Account
        fields = ['username','first_name', 'last_name', 'street_number', 'street_name',
                    'suburb', 'state', 'car_license', 'password1', 'password2']
