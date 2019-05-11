from django.db import models
from django.contrib.auth.models import User


# Our Account Model
class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	book_status = models.BooleanField(default=False)
    # Personal Information
	mobile = models.CharField(max_length=10)
	car_license = models.CharField(max_length=7)
	# location information
	street_number = models.CharField(max_length=4)
	street_name = models.CharField(max_length=20)
	suburb = models.CharField(max_length=12)
	postcode = models.CharField(max_length=4)
