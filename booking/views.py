from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from map.models import Car
from user.models import Account
from django.contrib.auth.models import User
from booking.models import Booking
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from decimal import Decimal
from django.urls import reverse
import stripe
import datetime
from django.utils import timezone

stripe.api_key = settings.STRIPE_SECRET_KEY

class BookingPage(TemplateView):
	template_name = 'booking/booking.html'

	# Recieving get request from form
	def get(self, request, number_plate):
		# if user book status is false, continue, else alert user

		account_user = Account.objects.get(user__username=request.user)
		if account_user.book_status == False:
			# Set car object using the number_plate
			set_car = Car.objects.get(number_plate=number_plate)

			if set_car.available == True:
				# Set the selected car to false so other users can't select the car
				# set_car.available = False
				# Save car object to database
				# set_car.save()
				args = {
	        		"car": set_car,
	    		}
			#if set_car is not available
			else:
				# add alert popup "Car is currently unavailable"
				args = {
					"message" : "Car is currently unavailable"
				}
				return redirect(reverse('home'))
		else:
			# User has booked a car already, send an alert
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		return render(request, self.template_name, args)


class ConfirmationPage(TemplateView):
	template_name = 'booking/confirmation.html'

	def get(self, request):
		# when user enters url instead through booking, redirect to homepage
		return redirect(reverse('home'))

	def post(self, request):

		# Get the number plate posted
		number_plate = request.POST.get("number_plate", "value")
		
		# Get car object using number plate
		booked_car = Car.objects.get(number_plate=number_plate)

		args = {
			"car": booked_car
		}

		return render(request, self.template_name, args)

class SuccessPage(TemplateView):
	template_name = 'booking/success.html'

	def get(self, request):
		print("GET success")
		# when user enters url instead through booking, redirect to homepage
		return redirect(reverse('home'))

	def post(self, request):
		if request.method == 'POST':
			token = request.POST.get('stripeToken', False)
			if token:
				# Get current user
				user  = request.user

				# Create a Customer:
				customer = stripe.Customer.create(
					source=token,
					email=user.email,
				)

				# Charge the Customer instead of the card:
				charge = stripe.Charge.create(
					amount=1000,
					currency='aud',
					customer=customer.id,
				)

				# Get the number plate posted
				number_plate = request.POST.get("number_plate", "value")

				# Get car object using number plate
				booked_car = Car.objects.get(number_plate=number_plate)

				# Initialize booking
				booking = Booking.objects.create(brand=booked_car.brand, transmission=booked_car.transmission, number_plate=booked_car.number_plate,
										price=booked_car.price, start_latitude=booked_car.latitude, start_longitude=booked_car.longitude, user=user)

				# Recording customer_id for charging payment later
				booking = Booking.objects.all().filter(user_id=request.user.id).order_by("-id")[0]
				booking.customer_id = customer.id
				booking.save()

				# Update user's book status in Account model database
				user.account.book_status = True
				user.save()

		return render(request, self.template_name)
