from django.db import models
from django.contrib.auth.models import User


# Our Account Model
class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	book_status = models.BooleanField(default=False)
	# personal information
	first_name = models.CharField(max_length=12)
	last_name = models.CharField(max_length=12)
	# GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	# mobile = models.CharField(max_length=10)
	car_license = models.CharField(max_length=7)
	# location information
	street_number = models.CharField(max_length=4)
	street_name = models.CharField(max_length=12)
	suburb = models.CharField(max_length=12)
	STATE_CHOICES = (
        ('VIC', 'Victoria'),
        ('NSW', 'New South Wales'),
		('QLD', 'Queensland'),
		('TAS', 'Tasmania'),
		('SA', 'South Australia'),
		('ACT', 'Australia Captial Territory'),
		('NT', 'Northern Territory'),
		('WA', 'Western Australia')
    )
	state = models.CharField(max_length=3, choices=STATE_CHOICES)
	postcode = models.CharField(max_length=4)
