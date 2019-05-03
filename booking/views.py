from django.shortcuts import render, redirect
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
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

	def payment(request):
		set_car = Car.objects.get(number_plate=number_plate)
		publishKey = settings.STRIPE_PUBLISHABLE_KEY
		if request.method == 'POST':
			print('test')
			token = request.POST.get('stripeToken', False)
			print('test')
			if token:
				try:
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
					return redirect(reverse('home',
							kwargs={
								'token': token
							})
						)
				except stripe.CardError as e:
					message.info(request, "Your card has been declined.")
		context = {
			'order': existing_order,
			'client_token': client_token,
			'STRIPE_PUBLISHABLE_KEY': publishKey
		}

		return render(request, self.template_name, context)

	def get(self, request, number_plate):
		set_car = Car.objects.get(number_plate=number_plate) # Set car object using the number_plate
		args = {
        	"car": set_car,
    	}
		return render(request, self.template_name, args)
