from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Our Account Model
class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	book_status = models.BooleanField(default=False)
    # Personal Information
	mobile = models.CharField(max_length=10, validators=[RegexValidator(regex='^[0-9]{10}$', message="Mobile Number is incorrect", code='invalid_email')])
	car_license = models.CharField(max_length=7, validators=[RegexValidator(regex='^[0-9]{7}$', message="Postcode is incorrect", code='invalid_license')])
	# location information
	street_number = models.CharField(max_length=4, validators=[RegexValidator(regex='^[0-9]+[a-z]*$', message="Street Number is incorrect", code='invalid_street_number')])
	street_name = models.CharField(max_length=20, validators=[RegexValidator(regex='(^[a-zA-Z]+$)|(^[a-zA-Z]+\s[a-zA-Z]+$)', message="Street name is incorrect", code='invalid_street_name')])
	suburb = models.CharField(max_length=12, validators=[RegexValidator(regex='(^[a-zA-Z]+$)|(^[a-zA-Z]+\s[a-zA-Z]+$)', message="Suburb is incorrect", code='invalid_suburb')])
	postcode = models.CharField(max_length=4, validators=[RegexValidator(regex='^[0-9]{4}$', message="Postcode is incorrect", code='invalid_postcode')])


	# (^[a-zA-Z]+$)|(^[a-zA-Z]+\s[a-zA-Z]+$)
	#
