from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from django.urls import reverse
from booking.models import Booking
import datetime
import stripe

class UserDashPage(TemplateView):
	template_name = 'user/userdash.html'

	def get(self, request):

		user = request.user

		# Get the current user logged in and their current booking
		# if user.account.book_status == True:
		curr_booking = Booking.objects.all().filter(user_id=user.id).order_by("-id")[0]

		args = {
			"booking": curr_booking,
		}

		return render(request, self.template_name, args)

	def post(self, request):
		if request.method == 'POST':

			# Get current user's booking
			user = request.user
			curr_booking = Booking.objects.all().filter(user_id=user.id).order_by("-id")[0]

			# Get and save booking end date and time to booking model
			curr_booking.end_date = datetime.date.today()
			curr_booking.end_time = datetime.datetime.now().time()
			curr_booking.save()

			# Calculate price for booking
			start = datetime.datetime.combine(curr_booking.start_date, curr_booking.start_time)
			end = datetime.datetime.combine(curr_booking.end_date, curr_booking.end_time)
			time_difference = end - start
			seconds = time_difference.total_seconds()

			# Determine hours and minutes rounded with 2 decimal places
			duration = round((seconds/60/60), 2)

			# Determine price subtracting initial $10 booking deposit fee and round to nearest dollar
			price_in_dollars = round((duration * curr_booking.price) - 10, 0)

			# Convert to cents for stripe format
			price_in_cents = int(price_in_dollars * 100)

			# Charge the Customer instead of the card:
			charge = stripe.Charge.create(
				amount=price_in_cents,
				currency='aud',
				customer=curr_booking.customer_id,
			)

			return render(request, self.template_name)
