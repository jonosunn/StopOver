# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from django.urls import reverse
from user.forms import AccountForm, UserForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from booking.models import Booking
from map.models import Car
import datetime
import stripe
from django.contrib import messages

class UserDashPage(TemplateView):
	template_name = 'user/userdash.html'

	def get(self, request):

		user = request.user

		# Get user's current booking and booking history
		booking_history = None
		curr_booking = None

		if user.account.book_status == True:
			curr_booking = Booking.objects.all().filter(user_id=user.id).order_by("-id")[0]
			booking_history = Booking.objects.all().filter(user_id=user.id).order_by("-id")[1:]
		else:
			booking_history = Booking.objects.all().filter(user_id=user.id).order_by("-id")

		args = {
			"booking": curr_booking,
			"booking_history": booking_history
		}

		return render(request, self.template_name, args)

	def post(self, request):

		if request.POST['action'] == 'Return Car':

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

			# Charge user for minimum 1 hour booking
			if seconds < 3600:
				seconds = 3600

			# Determine hours and minutes rounded with 2 decimal places
			duration = round((seconds/60/60), 2)

			# Determine price subtracting initial $10 booking deposit fee and round to nearest dollar
			price_in_dollars = int(round((duration * curr_booking.price) - 10))

			# Convert to cents for stripe format
			price_in_cents = price_in_dollars * 100

			# Save actual price paid to database
			curr_booking.actual_price = price_in_dollars + 10
			curr_booking.save()

			# Charge the Customer instead of the card:
			charge = stripe.Charge.create(
				amount=price_in_cents,
				currency='aud',
				customer=curr_booking.customer_id,
			)

			# Update user's book status in Account model database
			user.account.book_status = False
			user.save()

			# Change status of car available to true
			booked_car = Car.objects.get(number_plate=curr_booking.number_plate)
			booked_car.available = True
			booked_car.save()

			args = {
				'curr_booking': curr_booking

			}

			return render(request, "user/return_success.html", args)

		elif request.POST['action'] == 'Update': 
			
			# Get the user
			curr_user = request.user

			if request.POST['email']:
				curr_user.email = request.POST['email']

			if request.POST['card-holder-name']:
				curr_user.account.car_license_name = request.POST['card-holder-name']

			if request.POST['card-number']:
				curr_user.account.car_license = request.POST['card-number']

			if request.POST['userStreetNo']:
				curr_user.account.street_number = request.POST['userStreetNo']

			if request.POST['userAddress']:
				curr_user.account.street_name = request.POST['userAddress']

			curr_user.save()
			return render(request, 'map/homepage.html')


class RegisterPageView(TemplateView):
	template_name = 'user/register.html'

	def post(self, request):
		account_form = AccountForm(request.POST)
		user_form = UserForm(request.POST)

		if account_form.is_valid() and user_form.is_valid():
			# save user details, but don't add to database yet
			user = user_form.save(commit=False)
			# save username as email
			user.username = user.email
			# save user to user database
			user.save()
			# save account detail, but don't add to database
			account = account_form.save(commit=False)
			# add user to account
			account.user = user
			# save account to account database
			account.save()
			# Redirect to login page
			return redirect(reverse('login'))
		else:
			# Make new form
			account_form = AccountForm()
			user_form = UserForm()

			args = {
				'account_form' : account_form,
				'user_form' : user_form
			}

			return render(request, self.template_name, args)

	def get(self, request):
		# if user is not login
		if request.user.is_authenticated == False:
			user_form = UserForm()
			account_form = AccountForm()

			args = {
				'account_form' : account_form,
				'user_form' : user_form,
			}

			return render(request, self.template_name, args)
		else:
			# user is logged in, redirect to home
			return redirect(reverse('home'))


class LoginPageView(LoginView):
	# Changed label from username to email for login
    authentication_form = CustomAuthenticationForm
