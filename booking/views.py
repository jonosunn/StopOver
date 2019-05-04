from django.shortcuts import render, redirect
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class BookingPage(TemplateView):
	template_name = 'booking/booking.html'

	# Recieving get request from form
	def get(self, request, number_plate):
		# Set car object using the number_plate
		set_car = Car.objects.get(number_plate=number_plate)
		# Set the selected car to false so other users can't select the car
		# set_car.available = False
		# Save car object to database
		# set_car.save()

		args = {
        	"car": set_car,
    	}
		return render(request, self.template_name, args)


class ConfirmationPage(TemplateView):
	template_name = 'booking/confirmation.html'

	#TODO: SET CORRECT URLS
	# @csrf_exempt
	# def post(self, request):
	# 	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	# 	print('test')
	# 	if request.method == 'POST':
	# 		print('test')
	# 		token = request.POST.get('stripeToken', False)
	# 		print('test')
	# 		if token:
	# 			print('test1')
	# 			try:
	# 				print('test2')
	# 				# Create a Customer:
	# 				customer = stripe.Customer.create(
	# 					source=token,
	# 					email='paying.user@example.com',
	# 				)
	#
	# 				# Charge the Customer instead of the card:
	# 				charge = stripe.Charge.create(
	# 					amount=1000,
	# 					currency='aud',
	# 					customer=customer.id,
	# 				)
	# 				return redirect(reverse('home',
	# 						kwargs={
	# 							'token': token
	# 						})
	# 					)
	# 			except stripe.CardError as e:
	# 				message.info(request, "Your card has been declined.")
	# 	context = {
	# 		'STRIPE_PUBLISHABLE_KEY': publishKey
	# 	}
	#
	# 	return render(request, self.template_name, context)

	def get(self, request):
		print("GET METHOD")

		# Get the number plate posted
		number_plate = request.GET.get("number_plate", "value")

		# Get car object using number plate
		booked_car = Car.objects.get(number_plate=number_plate)
		args = {
			"car": booked_car
		}

		return render(request, self.template_name, args)

class SuccessPage(TemplateView):
	template_name = 'booking/success.html'

	def post(self, request): # new
		if request.method == 'POST':
			print('test')
			token = request.POST.get('stripeToken', False)
			print('test')
			if token:
				print('test1')
				print('test2')
				# Create a Customer:
				customer = stripe.Customer.create(
					source=token,
					email='paying.user@example.com',
				)

				# Charge the Customer instead of the card:
				charge = stripe.Charge.create(
					amount=1000,
					currency='aud',
					customer=customer.id,
				)

		return render(request, self.template_name)
