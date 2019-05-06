from django.db import models
from django.contrib.auth.models import User

# Our Booking Model
class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	start_date = models.DateField(auto_now_add=True)
	start_time = models.TimeField(auto_now_add=True)
	end_date = models.DateField()
	end_time = models.TimeField()

	# Customer id for payment
	customer_id = models.CharField(max_length=250)

	# Static car details for the booking
	brand = models.CharField(max_length=20)
	transmission = models.CharField(max_length=20)
	number_plate = models.CharField(max_length=7)
	price = models.IntegerField()
	longitude = models.FloatField()
	latitude = models.FloatField()
